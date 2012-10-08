# arrest - a REST client

_arrest_ is a JSON REST client designed to be as easy to use as possible.

    import arrest
    api = arrest.Client("http://some.api/1.0")

    ### GET a JSON object from http://some.api/1.0/stuff
    object = api.stuff(arg="foo")

    ### GET a JSON object from http://some.api/1.0/things/and/stuff
    object = api.things.and.stuff(arg="foo")

    ### GET http://some.api/1.0/things/all
    api.things.all()

    ### POST a JSON object to http://some.api/1.0/do_stuff
    api.do_stuff({store: this_object})

    ### PUT to http://some.api/1.0/new/thing
    api.new.thing = {store: "a new thing"}

    ### DELETE http://some.api/1.0/old/thing
    del api.old.thing

See the docstrings in arrest.py for more examples.

That's it.
