"""Template method article parser"""
from abc import ABC, abstractmethod
import logging
from newspaper import Article, Config


logging.basicConfig(level=logging.INFO)


class AbstractArticleParser(ABC):
    """Abstract article parser"""
    article: Article

    """Abstract Article Parser Class

    Args:
        ABC (class): Helper class
    """
    def __init__(self, url: str) -> None:
        self.url = url

    async def get_article(self):
        """Template method"""
        await self.load_article()
        await self.read_article()

    async def load_article(self) -> None:
        """Load and parse article"""
        config = Config()
        config.memoize_articles = False

        article = Article(self.url, config=config)
        article.download()
        article.parse()

        self.article = article

    @abstractmethod
    async def read_article(self):
        """Read article and return content"""
        ...
