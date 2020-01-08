class Article:
    """
    represents single parsed article
    """
    def __init__(self, title, author, url, tags):
        self.title = title
        self.author = author
        self.url = url
        self.tags = tags

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_url(self):
        return self.url

    def get_tags(self):
        return self.tags
