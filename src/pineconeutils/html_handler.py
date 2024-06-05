import os
from llama_index.readers.web import SimpleWebPageReader


class HTMLHandler:
    def __init__(self, urls):
        self.urls = urls

    def read_html(self):
        documents = SimpleWebPageReader(html_to_text=True).load_data(self.urls)
        return documents

