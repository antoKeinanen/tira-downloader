# Tira Downloader

## Overview

Tira Downloader is a simple web scraper designed to download all the boilerplate code for Data Structures and Algorithms (**TI**eto**R**akenteet ja **A**lgoritmit) courses from the University of Helsinki's ECSC system.

This script automates the retrieval of task boilerplates, saving them in structured directories for easy access and organization.

## Features

- Scrapes task lists from the ECSC system.
- Extracts and downloads boilerplate code for each task.
- Saves files in structured directories based on course name and task title.
- Skips already downloaded files to prevent duplicates.

## Requirements

Ensure you have the following dependencies installed:

- Python ^3.9
- `requests` library
- `beautifulsoup4` library

You can install the required dependencies using:

```bash
pip install requests beautifulsoup4
```

or with Poetry:

```bash
poetry install
poetry run python main.py
```

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/tira-downloader.git
   cd tira-downloader
   ```
2. Run the script:
   ```bash
   python tira_downloader.py
   ```
3. Enter the course name (e.g., `tira25k`) when prompted.
4. The script will scrape and download the necessary boilerplates, organizing them into directories.

## Example Output

```
Course name (i.e. tira25k): tira25k
 [i] INFO: Downloading task list...
 [i] INFO: Scraping task details...
 [i] INFO: Saving boilerplates...
 [i] INFO: Done!
```

## Directory Structure

After running the script, the files are organized as follows:

```
./tira25k
├── viikko1
│   ├── boxes.py
│   ├── segments.py
│   ├── special.py
│   ├── student.py
│   ├── twodigit.py
│   └── wordgrid.py
├── viikko2
│   ├── circlegame.py
│   ├── fastrounds.py
│   ...
...
```

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests. Although I do not plan to actively maintain this project, I will review and accept pull requests.

## License

This project is licensed under the MIT License.
