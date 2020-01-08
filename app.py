from Utils import Utils
from pathlib import Path
from Selectors import ArticleSelectors
from parsers.ArticleListParser import ArticleListParser


def start_scraping():
    url = 'https://www.aljazeera.com/indepth/opinion/'
    parser = ArticleListParser(url, ArticleSelectors.ARTICLE_LINK)
    articles = parser.parse_article_list()

    Utils.save_to_file(articles)


FILE_NAME = 'articles.json'
data_file = Path(FILE_NAME)

# if json file exists, plot the graph
# otherwise start scraping
if data_file.exists():
    Utils.draw_charts(FILE_NAME)
else:
    start_scraping()
    Utils.draw_charts(FILE_NAME)


