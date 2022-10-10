import copy
import logging

from scrapy.spiders import CrawlSpider, Rule


class BadatelSpider(CrawlSpider):
    name = "badatel"
    home_page = "https://www.badatel.net/"
    allowed_domains = ["badatel.net"]
    start_urls = ["https://www.badatel.net"]

    def __init__(self, *args, **kwargs):
        """Function is called when the spider is initialized

        Keyword arguments:
        args -- full paths of start urls with protocol (http, https), separated by ','
        """

        home_page = "https://www.badatel.net"

        self.data_provider_id = kwargs.pop('data_provider_id')



