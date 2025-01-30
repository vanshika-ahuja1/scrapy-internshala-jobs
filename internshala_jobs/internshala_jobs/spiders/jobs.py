import scrapy
from internshala_jobs.items import InternshalaJobsItem


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["internshala.com"]
    start_urls = ["https://internshala.com/jobs/page-1/"]

    def parse(self, response):
        job_listings=response.xpath("//div[@class='internship_meta experience_meta']")
        for job in job_listings:
            item = InternshalaJobsItem()

            #job title
            job_title=job.xpath(".//h3[@class='job-internship-name']/a[@class='job-title-href']/text()").get()
            item['job_title']=job_title.strip() if job_title else ''
            
            #company name
            company=job.xpath(".//div[@class='company_and_premium']/p[@class='company-name']/text()").get()
            item['company']=company.strip() if company else ''

            #job location
            location=job.xpath(".//div[@class='detail-row-1']/p[@class='row-1-item  locations']/span/a/text()").get()
            item['location']=location.strip() if location else ''

            #job posted date
            posted_date=job.xpath(".//div[@class='status-success']/span/text()").get()
            item['posted_date']=posted_date.strip() if posted_date else ''

            #job stipend amount
            stipend=job.xpath(".//div[@class='detail-row-1']/div[@class='row-1-item']/span[@class='desktop']/text()").get()
            item['stipend']=stipend.strip() if stipend else ''

            yield item
        
        #for next page
        current_page_number = int(response.url.split('page-')[-1].split('/')[0])

        # Generate the next page URL dynamically based on the current page number
        next_page_number = current_page_number + 1
        next_page_url = f'https://internshala.com/jobs/page-{next_page_number}/'

        # Check if the next page exists by verifying if job listings are present
        next_page_exists = response.xpath("//div[@class='internship_meta experience_meta']").get()

        if next_page_exists:
            yield scrapy.Request(next_page_url, callback=self.parse)
        else:
            self.log("No more pages to scrape. Stopping the crawl.")


