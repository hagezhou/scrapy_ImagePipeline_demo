# -*- coding: utf-8 -*-
import scrapy
from downLoadImg.items import DownloadimgItem

class DownimgSpider(scrapy.Spider):
    name = "downImg"
    allowed_domains = ["xeall.com"]
    start_urls = (
        'http://www.xeall.com/shenshi/12776_3.html',
    )

    # /[@id="mh_content"]//ul/li//p/@src
    def parse(self, response):
        item_obj = DownloadimgItem()
        href = response.xpath('//li[@id="imgshow"]/p/img/@src')
        item_obj["image_urls"] = href.extract()

        yield item_obj
