from news_scraper import news_scraper

import requests
from bs4 import BeautifulSoup


class coindesk(news_scraper):

    def get_articles(self):
        response = requests.get('https://www.coindesk.com/')

        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find_all(class_="heading")
        
        headers = map(lambda a: a.text, articles)
        return(headers)


if __name__ == "__main__":
    cd = coindesk()
    for article in cd.get_articles():
        print(article)