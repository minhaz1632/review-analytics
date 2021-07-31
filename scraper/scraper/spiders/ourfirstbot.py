import scrapy


class OurfirstbotSpider(scrapy.Spider):
    name = 'ourfirstbot'
    start_urls = ['https://www.yelp.com/biz/cuisine-of-nepal-san-francisco']
    start = 0
    step = 10
    has_more_reviews = True

    def parse(self, response):
        ratings = response.xpath("//li//div[contains(@class, 'i-stars')]")
        comments = response.css("li p[class*=comment]>span").extract()
        dates = response.xpath(
            "//div[contains(@class, 'review')]/div[position()=2]//div[position()=2]/span/text()"
        ).extract()
        reviewer = response.xpath(
            "//li//div[contains(@class, 'review')]/div[position()=1]//"
            "div[contains(@class, 'user-passport-info')]/span//text()"
        ).extract()
        reviewer_address = response.xpath(
            "//li//div[contains(@class, 'review')]/div[position()=1]//"
            "div[contains(@class, 'user-passport-info')]//div/span//text()"
        ).extract()

        if len(ratings) == 0:
            self.has_more_reviews = False

        for item in zip(ratings, comments, dates, reviewer, reviewer_address):
            yield {
                'rating': item[0].attrib['aria-label'],
                'comment': item[1],
                'date': item[2],
                'reviewer': item[3],
                'reviewer_address': item[4],
            }

        # yield {
        #     'ratings': len(ratings),
        #     'comments': len(comments),
        #     'dates': len(dates),
        #     'reviewer': len(reviewer),
        #     'reviewer_address': len(reviewer_address),
        # }

        if self.has_more_reviews:
            self.start = self.start + self.step
            next_page_url = f'{self.start_urls[0]}?start={self.start}'
            print(next_page_url)
            yield response.follow(next_page_url, callback=self.parse)

