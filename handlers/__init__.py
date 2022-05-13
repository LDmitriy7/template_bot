from . import for_admins


def setup():
    from . import errors

    from . import start
    from . import fallbacks

    for_admins.setup()

    from . import misc
