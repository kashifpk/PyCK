"""
Multiple item selector mako module
------------------------------------

Allows displaying multiple items and select one or many from the list
"""

from mako.template import Template

from .template_lookup import template_lookup

import sys
PY3 = sys.version > '3'


def multi_selector(items, ignore_prefix=None):
    """
    Displays given items for multi-selection
    
    :param items: A dictionay or dictionary-like object. Key is returned on form submission, value is displayed
    :ignore_prefix: (optional) if given key names starting with the prefix are not displayed (ignored)
    
    """
    
    tmpl = template_lookup.get_template("multi_selector.mako")
    output = tmpl.render(items=items, ignore_prefix=ignore_prefix)

    if PY3:
        output = output.decode('utf-8')

    return output
