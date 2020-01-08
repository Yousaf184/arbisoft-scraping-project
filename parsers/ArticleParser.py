from Selectors import ArticleSelectors
from Article import Article


class ArticleParser:
    """
    responsible for parsing single article
    """
    def __init__(self, article, article_url):
        self.article = article
        self.article_url = article_url

    def title(self):
        title = self.article.find_element_by_css_selector(ArticleSelectors.ARTICLE_TITLE)
        return title.text

    def author_name(self):
        name = self.article.find_element_by_css_selector(ArticleSelectors.ARTICLE_AUTHOR)
        return name.text

    def tags(self):
        tags = self.article.find_elements_by_css_selector(ArticleSelectors.ARTICLE_TAGS)
        tag_list = []

        for tag in tags:
            tag_list.append(tag.text)

        return tag_list

    def parse_article(self):
        title = self.title()
        author = self.author_name()
        url = self.article_url
        tag_list = self.tags()

        return Article(title, author, url, tag_list)




