from news_scraper import news_scraper
from coindesk_scraper import coindesk

class news(news_scraper):

    def __init__(self) -> None:
        self.news_scrapers = {}
        self.news_scrapers['coindesk'] = coindesk()

    def get_articles(self):
        articles = []
        for site in self.news_scrapers:
            scraper = self.news_scrapers[site]
            articles.extend(scraper.get_articles())
        return articles


if __name__ == "__main__":
    n = news()
    print(n.get_articles())