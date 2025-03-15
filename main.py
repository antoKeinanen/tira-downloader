import re
import requests
from os import makedirs, path
from bs4 import BeautifulSoup

BASE_URL = "https://cses.fi"


def scrape_task_details(task_href):
    r = requests.get(f"{BASE_URL}{task_href}")

    if not r.ok:
        raise RuntimeError(r)

    soup = BeautifulSoup(r.content, "html.parser")
    boilerplate = soup.find("pre", class_="prettyprint")
    filenames = [c.text for c in soup.find_all("code") if re.search(r"\.py", c.text)]
    if len(filenames) != 1:
        print(
            f"\033[33m [!] WARNING: Could not determine filename for {BASE_URL}{task_href} \033[0m"
        )
        return
    if not boilerplate:
        print(
            f"\033[33m [!] WARNING: Could not scrape boilerplate for {BASE_URL}{task_href} \033[0m"
        )
        return

    filename = filenames[0]
    return (filename, boilerplate.text)


def scrape_task_list(course_name):
    print("\033[97m [i] INFO: Downloading task list...\033[0m")

    r = requests.get(f"{BASE_URL}/{course_name}/list")

    if not r.ok:
        raise RuntimeError(r)

    soup = BeautifulSoup(r.content, "html.parser")
    task_lists = soup.find_all("ul", class_="task-list")
    titles = soup.find_all("h2")


    print("\033[97m [i] INFO: Scraping task details...\033[0m")
    task_list = []
    for title, tasks in zip(titles, task_lists):
        title = title.text
        if not re.search(r"\d", title):
            continue
        task_hrefs = [t.attrs.get("href") for t in tasks.find_all("a")]
        for task_href in task_hrefs:
            details = scrape_task_details(task_href)
            if details:
                stripped_title = re.sub(r"\s+", "", title).lower()
                task_list.append((stripped_title, *details))

    return task_list


def write_files(course_name, task_list):
    print("\033[97m [i] INFO: Writing boilerplates...\033[0m")

    for title, task_filename, boilerplate in task_list:
        dirpath = f"./{course_name}/{title}"
        filepath = f"{dirpath}/{task_filename}"
        if not path.exists(filepath):
            makedirs(dirpath, exist_ok=True)
            with open(filepath, "x") as file:
                file.write(boilerplate)
        else:
            print(
                f"\033[97m [i] INFO: {title}/{task_filename} already exists, skipping...\033[0m"
            )


if __name__ == "__main__":
    course_name = input("Course name (i.e. tira25k): ")
    task_list = scrape_task_list(course_name)
    write_files(course_name, task_list)

    print("\033[97m [i] INFO: Done!\033[0m")
