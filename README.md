# AmazonScraper Ninja

A flexible Python-based web scraper for extracting product reviews from Amazon using Selenium and BeautifulSoup.

## Features

- Scrapes multiple pages of reviews for any Amazon product
- Extracts reviewer name, date, package/model, star rating, and review text
- Saves data to a CSV file
- Handles dynamic page loading with scrolling

## Requirements

- Python 3.7+
- Chrome browser

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/amazonscraper-ninja.git
   cd amazonscraper-ninja
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Open the `scraper.py` file and modify the `base_url` variable with the URL of the Amazon product you want to scrape.

2. Run the script:
   ```
   python scraper.py
   ```

The script will start scraping reviews and save them to a CSV file named after the product in the same directory.

## Customization

You can easily modify the script to scrape different information or adjust the number of pages to scrape by editing the `scraper.py` file.

## Note

This script is for educational purposes only. Please respect Amazon's terms of service when using this scraper.