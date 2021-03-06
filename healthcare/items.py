# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HealthcareItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	id=scrapy.Field()
	keywords=scrapy.Field()
	description=scrapy.Field()
	url=scrapy.Field()
	title=scrapy.Field()
	source=scrapy.Field()
	content=scrapy.Field()
	author=scrapy.Field()
