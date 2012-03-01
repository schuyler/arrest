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
    >>> openlibrary = Client("http://openlibrary.org", ext="json")
    >>> book = openlibrary.books["OL3438168M"]
    >>> book["title"]
    u'Mapping hacks'
    >>> twitter = Client("http://search.twitter.com/", ext="json", params={'rpp':10})
    >>> search = twitter.search(q=u'flamb\xe9')
    >>> len(search["results"])
    10
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
        opts = self.__opts
        headers = {"Accept": "application/json"}
        request = data = None
        url = self.__path
        if opts.get("ext"): url += "." + opts["ext"]
        if args:
            data = json.dumps(args[0])
        else:
            params = opts["params"] if opts.get("params") else {}
            params.update(kwargs)
            for key, val in params.items():
                if hasattr(val, "encode"):
                    params[key] = val.encode("utf-8")
            if params: url += "?" + urllib.urlencode(params)
        request = urllib2.Request(url, data, headers)
        opener = urllib2.urlopen(request)
        content = opener.read()
        return json.loads(content)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
