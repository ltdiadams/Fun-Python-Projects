# Send in your proposal and get the project
# Python Scrapy

import scrapy
import re
from pdf_url.items import PdfUrlItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PdfUrlSpider(CrawlSpider):  # spiders are classes that crawl on our domain

    # This name is required. It is how we refer to this PdfUrlSpider class on the command line
    name = 'pdf_url'

    # Every link we look at MUST be a part of the adobe.com domain (i.e. contain "adobe.com" in its url)
    allowed_domains = ['arxiv.org']

    # This is the url we will start from (CHeck all the links on this webpage first, then go deeper)
    start_urls = ['https://arxiv.org/']

    # This Rule says:
    #  1. allow all links to be extracted
    #  2. call parse_httpresponse on each extracted link
    #  3. follow all links ("click" on them) so we can check all the links on THAT webpage too
    rules = [Rule(LinkExtractor(allow=''), callback='parse_httpresponse', follow=True)]

    def parse_httpresponse(self, response):
        # callback function (passing a function to a function) is going to start
        # scraping the website for us and putting it in a csv file
        if response.status != 200:
            return None

        print(response.url)
        # print()

        item = PdfUrlItem()

        # check if the link goes to a pdf
        if b'Content-Type' in response.headers.keys():
            links_to_pdf = 'application/pdf' in str(response.headers['Content-Type'])
            # print(links_to_pdf)
        else:
            return None

        # check if content disposition exists
        content_disposition_exists = b'Content-Disposition' in response.headers.keys()

        # If it does, scrape it
        if links_to_pdf:
            # scrape the specified data
            if content_disposition_exists:
                item['filename'] = re.search('filename="(.+)"', str(response.headers['Content-Disposition'])
                                             ).group(1)
                item['url'] = response.url

            item['filename'] = response.url.split('/')[-1]
            item['url'] = response.url

        # If not, ignore it and move on to the next link
        else:
            return None
        # write that data to the csv

        return item
