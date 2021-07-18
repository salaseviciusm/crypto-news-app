import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    response = requests.get('https://www.coindesk.com/')

    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all(class_="heading")
    for article in articles:
        print("-"*50)
        print(article.text)