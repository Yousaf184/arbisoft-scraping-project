import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Selectors import ArticleSelectors
from parsers.ArticleParser import ArticleParser


class ArticleListParser:
    """
    responsible for parsing web page containing list of articles
    """
    def __init__(self, page_url, article_link_selector):
        self.page_url = page_url
        self.article_link_selector = article_link_selector

    def parse_article_list(self):
        print('scraping start...')
        options = Options()
        options.headless = True

        browser = webdriver.Chrome(chrome_options=options)
        browser2 = webdriver.Chrome(chrome_options=options)

        browser.get(self.page_url)

        print('loading articles...')
        ArticleListParser.load_more_articles(browser)
        print('articles loaded...')

        articles = browser.find_elements_by_css_selector(self.article_link_selector)
        print(f'total articles loaded = {len(articles)}')

        article_list = []
        article_counter = 1

        for article in articles:
            if article_counter % 5 == 0:
                time.sleep(3)

            print(f'scraping article no: {article_counter}')
            article_counter += 1

            # get complete article link
            article_url = article.get_attribute('href')
            # download article web page
            browser2.get(article_url)
            # get parsed article
            parsed_article = ArticleParser(browser2, article_url).parse_article()
            article_list.append(parsed_article)

        print('scraping done')
        return article_list

    # press 'show more' button on articles list page
    # more around 50 times so that around 500 articles are loaded
    # on the web page
    @classmethod
    def load_more_articles(cls, browser):
        no_of_page_downs = 1

        while no_of_page_downs <= 54:
            time.sleep(3)
            print(f'loading page no: {no_of_page_downs}')
            show_more_btn = browser.find_element_by_id(ArticleSelectors.SHOW_MORE_BTN_ID)
            browser.execute_script("arguments[0].click();", show_more_btn)
            no_of_page_downs += 1
