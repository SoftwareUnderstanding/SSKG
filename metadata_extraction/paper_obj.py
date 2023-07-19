
import re
from utils.regex import str_to_doiID, str_to_arxivID

class PaperObj:
    def __init__(self, title, code_urls, doi, arxiv, file_name, file_path):
        self._title = title
        self._code_urls = code_urls
        self._doi = str_to_doiID(doi)
        self._arxiv = str_to_arxivID(arxiv)
        self._file_name = file_name
        self._file_path = file_path

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def code_urls(self):
        return self._code_urls

    @code_urls.setter
    def code_urls(self, value):
        self._code_urls = value

    @property
    def doi(self):
        return self._doi

    @doi.setter
    def doi(self, value):
        self._doi = value

    @property
    def arxiv(self):
        return self._arxiv

    @arxiv.setter
    def arxiv(self, value):
        self._arxiv = value

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value

    def to_dict(self):
        return {
            'title': self._title,
            'code_urls': self._code_urls,
            'doi': self._doi,
            'arxiv': self.arxiv,
            'file_name': self._file_name,
            'file_path': self._file_path
        }