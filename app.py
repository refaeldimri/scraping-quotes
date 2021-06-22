import requests
from pages.quotesPage import QuotesPage

pageContents = requests.get('https://quotes.toscrape.com/').content
page = QuotesPage(pageContents)

for quote in page.quotes:
    print(quote.content)




