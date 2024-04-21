# Manga Scraper

Manga Scraper is a simple Python script for scraping manga chapters from online manga websites. It allows users to specify the name of the manga and provide an input file containing the URLs of manga chapters to be downloaded.

## Installation

To install the Manga Scraper, you'll need Python 3 and pip installed on your system.

1. Clone the repository:
```bash
   git clone https://github.com/EdgeLordKirito/MangaWebScraper.git
```
2. Install project dependencies:
``` bash
   cd MangaWebScraper
   
   pip install -r requirements.txt
```
3. On Linux, set execute permission for the shell script:
```bash
   chmod +x run_manga_scraper.sh
```

## How to Use

To use the Manga Scraper, follow these steps:
### Unix/Linux:

1. Run the main script with the manga name and input file:
```bash
   ./run_manga_scraper.sh <name> <input_file>
```

### Windows:

1. Run the main script with the manga name and input file:
```batch
   run_manga_scraper.bat <name> <input_file>
```

-  Replace `<name>` with the name of the manga. This will be used to create a folder containing the sub folders for each chapter's pages.
- `<input_file>` should be a basic text file containing a single URL per line. Each URL should point to a web page containing the pages of a manga chapter.