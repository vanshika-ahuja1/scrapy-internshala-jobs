# Scrapy Internshala Jobs Scraper

This is a Scrapy spider designed to scrape job listings from **Internshala**. The spider is specifically built to extract job information like job title, company name, location, stipend, posted date from the Internshala job listings.

## Table of Contents
* Description
* Features
* Installation
* Usage
* Output
  
## Description
The Internshala Jobs Scraper is a Python-based scraping project that uses Scrapy to extract data from the Internshala Jobs website. This spider can crawl through multiple pages of job listings and extract information such as:

* Job Title
* Company Name
* Job Location
* Posted Date
* Stipend Offered
The spider is configured to follow pagination automatically, scraping all available pages of jobs up to a certain limit.

## Features
* Scrapes job listings from Internshala.
* Extracts key job information: title, company, location, posted date, and stipend.
* Handles multiple pages through pagination.
* Clean data output in CSV format.
* Uses Scrapy framework for efficient web scraping.
* Can be easily customized for additional fields.

## Installation

**Step 1:** Install Python and Virtual Environment (if not installed)
* Make sure you have Python 3.x installed. You can check this by running:
```
python --version
```
* To set up a virtual environment (recommended), run:
```
python -m venv .venv
source .venv/bin/activate  # For Mac/Linux
.venv\Scripts\activate     # For Windows
```

**Step 2:** Install Scrapy
In your virtual environment, install Scrapy by running:
```
pip install scrapy
```

## Usage

**Step 1:** Clone the Repository
Clone the repository to your local machine:
```
git clone https://github.com/vanshika-ahuja1/scrapy-internshala-jobs.git
cd scrapy-internshala-jobs
```

**Step 2:** Run the Spider
To run the spider and start scraping:
```
scrapy crawl jobs -o jobs.csv
```
This will start the spider and output the scraped job listings in a CSV file named `jobs.csv`.

## Output

The output is saved in CSV format and will include the following columns:

* job_title: The title of the job/internship.
* company: The company offering the job.
* location: The location of the job.
* posted_date: The date when the job was posted.
* stipend: The stipend offered for the job/internship.

