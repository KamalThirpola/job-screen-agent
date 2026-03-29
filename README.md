# Job Screen Agent

This project is an automated agent built using Python and Playwright.

## Features

* Reads job URLs from an Excel file
* Opens each URL automatically in a browser
* Takes full-page screenshots
* Handles failures without stopping execution
* Saves screenshots for all successful URLs

## Tech Stack

* Python
* Playwright
* OpenPyXL

## How to Run

1. Install dependencies:
   pip install playwright openpyxl

2. Install browsers:
   playwright install

3. Run the script:
   python main.py

## Output

Screenshots are saved as:

* screenshot_1.png
* screenshot_2.png
* screenshot_3.png
* screenshot_4.png
