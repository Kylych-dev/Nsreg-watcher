# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

from ..utils import find_price_sub


REGEX_PATTERN = r".*(\d+\s+\d+).*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class NsregBitnamesSpider(scrapy.Spider):
    name = "nsreg_bitnames"
    allowed_domains = ["bitnames.ru"]
    start_urls = ["https://bitnames.ru/#features-2"]

    def parse(self, response):
        pricereg = response.xpath('//*[@id="features-2"]/div/div/div[1]/div/p/text()').get()
        pricereg = find_price_sub(REGEX_PATTERN, pricereg)
        
        priceprolong = response.xpath('//*[@id="features-2"]/div/div/div[2]/div/p/text()').get()
        priceprolong = find_price_sub(REGEX_PATTERN, priceprolong)

        pricechange = response.xpath('//*[@id="features-2"]/div/div/div[3]/div/p/text()').get()
        pricechange = find_price_sub(REGEX_PATTERN, pricechange)

        item = NsregItem()
        item['name'] = "ООО «БИТНЭЙМС»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange 
        item['price'] = price

        yield item

