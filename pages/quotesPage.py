from bs4 import BeautifulSoup
from locators.quotesPageLocators import QuotesPageLocators
from parsers.quote import QuoteParser

class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quotesTags = self.soup.select(locator)
        return [QuoteParser(q) for q in quotesTags]
