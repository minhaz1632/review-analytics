from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess

from scraper.scraper.spiders.ourfirstbot import OurfirstbotSpider


class Command(BaseCommand):
    help = 'Receives url and run spider'

    # def add_arguments(self, parser):
        # parser.add_argument('poll_ids', nargs='+', type=str)

    def handle(self, *args, **options):
        process = CrawlerProcess({
            'LOG_LEVEL': 'WARNING',
            'ITEM_PIPELINES': {
                'scraper.scraper.pipelines.ScraperPipeline': 300,
            }
        })
        process.crawl(OurfirstbotSpider)
        process.start()


