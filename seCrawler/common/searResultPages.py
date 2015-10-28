__author__ = 'tixie'

from searchEngines import SearchEngines


class searResultPages:
    totalPage = 0
    keyword = None,
    searchEngineUrl = None
    currentPage = 0
    searchEngine = None

    def __init__(self, keyword, searchEngine, totalPage):
        self.searchEngine = searchEngine.lower()
        self.searchEngineUrl = SearchEngines[self.searchEngine]
        self.totalPage = totalPage
        self.keyword = keyword
        print "total page:{0}".format(self.totalPage)

    def __iter__(self):
        return  self

    def _currentUrl(self):
        return self.searchEngineUrl.format(self.keyword, str(self.currentPage  * 10))

    def next(self):
        if self.currentPage < self.totalPage:
            url =  self._currentUrl()
            self.currentPage = self.currentPage + 1
            return  url
        raise StopIteration
