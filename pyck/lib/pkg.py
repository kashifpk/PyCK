"""
Packages related utility functions
"""

import pkgutil


def get_submodules(package):
    """
    Returns all sub-modules of a package also indicating if the module is also a package
    Return a list with each item being a dictionary with keys name (String) and is_package (Boolean)
    """

    ret = []

    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        #print "Found submodule %s (is a package: %s)" % (modname, ispkg)
        ret.append({'name': modname, 'is_package': ispkg})

    return ret
