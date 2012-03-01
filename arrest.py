import json, urllib, urllib2

class Client(object):
    """
    >>> openlibrary = Client("http://openlibrary.org")
    >>> unicode(openlibrary.books.OL3438168M)
    u'http://openlibrary.org/books/OL3438168M'
    >>> book = openlibrary.books.OL3438168M()
    >>> book["title"]
    u'Mapping hacks'
    >>> book = openlibrary.books["OL3438168M"]
    >>> book["title"]
    u'Mapping hacks'
    >>> openlibrary = Client("http://openlibrary.org", ext=True)
    >>> book = openlibrary.books["OL3438168M"]
    >>> book["title"]
    u'Mapping hacks'
    """

    def __init__(self, path, **opts):
        if path.endswith("/"): path = path[:-1]
        self.__path = path
        self.__opts = opts

    def __getattr__(self, name):
        if name.startswith("__"): return getattr(self, name)
        return type(self)(self.__path + "/" + name, **self.__opts)

    def __getitem__(self, name):
        return self.__getattr__(name)()

    def __unicode__(self):
        return self.__path

    def __call__(self, *args, **kwargs):
        headers = {"Accept": "application/json"}
        request = data = None
        url = self.__path
        if self.__opts.get("ext"): url += ".json"
        if args:
            data = json.dumps(args[0])
        else:
            url += "?" + urllib.urlencode(kwargs)
        request = urllib2.Request(url, data, headers)
        opener = urllib2.urlopen(request)
        content = opener.read()
        return json.loads(content)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
