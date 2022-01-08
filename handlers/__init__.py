def setup():
    from . import errors

    from . import start
    from . import fallbacks

    from . import for_admins
    for_admins.setup()

    from . import misc
