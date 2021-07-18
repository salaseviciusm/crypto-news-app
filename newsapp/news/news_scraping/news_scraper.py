from abc import ABC, abstractmethod

class news_scraper(ABC):
    
    @abstractmethod
    def get_articles(self):
        pass