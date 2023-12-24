# levels.fyi Web Crawler - 
![Python Version](https://img.shields.io/badge/python-v3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

This is a web crawler script to collect salary information from levels.fyi for major tech companies (Facebook, Apple, Amazon, Netflix, Google, Nvidia). The data is then stored in an Excel file for analysis.

## Description
This web crawler is developed by Alec and Leo for scraping salary data from levels.fyi. It fetches the most recent fifty records for each company from the website and saves the data in an Excel file.

## Requirements
Make sure you have the following Python packages installed:
```bash
pip install selenium pandas bs4 requests matplotlib
```
Also, download the latest version of [ChromeDriver](https://chromedriver.chromium.org/downloads) and place it in the same directory as the script.

## Usage

### Crawl Data
Run the script to initiate web crawling. The script will prompt you to choose the data source:

- **c/currently**: Crawl data from levels.fyi (default).
- **p/specify_path**: Specify the path of an existing Excel file.
- **d/default**: Use the default Excel file.

```bash
python levelsfyi_crawler.py
```

### Query Data

After crawling data, you can query the information. The script supports various commands:

- **max_tc**: Display the record with the maximum total compensation.
- **min_tc**: Display the record with the minimum total compensation.
- **median_tc**: Display the record with the median total compensation.
- **company [name]**: Display records for a specific company.
- **location [location]**: Display records for a specific location.
- **level [level]**: Display records for a specific level.
- **tag [tag]**: Display records for a specific tag.
- **yoe [years_of_experience]**: Display records for a specific years of experience.
- **filter [attribute value attribute value ...]**: Filter records based on attributes and values.

Add ```--plot``` at the end of the command to generate plots for the queried data.

### Exit
Type ```exit``` or ```quit``` to exit the script.

## Example
1. Run the script and choose to crawl data.
2. uery the crawled data:
    ```bash
    max_tc
    company Apple
    location CA --plot
    level L4
    tag AI --plot
    yoe 3
    filter company Apple location CA --plot
    ```

## Note
- The script will automatically create an Excel file named ```levels_fyi.xlsx``` in the same directory as the script if it does not exist.
- The script fetches the most recent fifty records for each company
- The crawled data is saved in an Excel file

Feel free to customize and extend the script based on your needs!

