class UrlTable:
    def __init__(self, urls):
        self.todo_list = []
        self.all_url = {}
        for url in urls:
            self.all_url[url] = 0