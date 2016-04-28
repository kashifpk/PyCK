"""
Multiple item selector mako module
------------------------------------

Allows displaying multiple items and select one or many from the list
"""

import logging
from collections import OrderedDict
from mako.template import Template
from pprint import pprint
from .template_lookup import template_lookup

import sys
PY3 = sys.version > '3'

log = logging.getLogger(__name__)


def _get_group_key(in_str):
    """if item name contains '.' then split on '.' and use first part as group key
    otherwise split on '_' or '-' respectively"""

    splitters = '._- '
    splitter = ''

    for sp in splitters:
        parts = in_str.split(sp)
        splitter = sp
        if len(parts) > 1:
            break

    if len(parts) > 1:
        return (parts[0], splitter)

    return (None, None)


def group_similar(items):
    "Group items with similar keys into sub-dictionary of the item"

    grouped_items = OrderedDict()

    current_group_key = None
    current_sub_items = OrderedDict()
    
    # TODO: Consider all splitters to be the same, don't create a new sub-group for a different splitter

    for k, v in items.items():

        group_key, splitter = _get_group_key(k)

        if not group_key:
            grouped_items[k] = v
        else:
            if group_key == current_group_key:
                current_sub_items[k] = v
            else:
                if current_group_key:
                    if current_group_key in grouped_items:
                        new_dict = OrderedDict({current_group_key: grouped_items[current_group_key]})
                        new_dict.update(current_sub_items)
                        grouped_items[current_group_key] = new_dict
                    else:
                        grouped_items[current_group_key] = current_sub_items
                current_group_key = group_key
                current_sub_items = OrderedDict({k: v})

    if current_group_key:
        if current_group_key in grouped_items:
            new_dict = OrderedDict({current_group_key: grouped_items[current_group_key]})
            new_dict.update(current_sub_items)
            grouped_items[current_group_key] = new_dict
        else:
            grouped_items[current_group_key] = current_sub_items

    # Merge back groups that contain only a single element
    # final_group_items = grouped_items
    final_group_items = OrderedDict()
    for k, v in grouped_items.items():
        if type(v) is OrderedDict:
            if len(v.keys()) != 1:
                final_group_items[k] = v
            else:
                nk, nv = list(v.items())[0]
                final_group_items[nk] = nv
        else:
            final_group_items[k] = v

    # print(final_group_items)

    return final_group_items


def multi_selector(items, field_name, ignore_prefix=None, do_auto_grouping=True):
    """
    Displays given items for multi-selection

    :param items: A dictionay or dictionary-like object. Key is returned on form submission, value is displayed
    :param ignore_prefix: (optional) if given key names starting with the prefix are not displayed (ignored)
    :param do_auto_grouping: Group similar items together and make them collapsable

    Done:

    * Ability to auto-detect grouping
    * Ability to toggle sub-item selections for checkboxes

    TODO:

    * Ability to allow single select (Radio buttons)
    * Ability to only display data (no checkboxes or radio buttons)
    """

    if do_auto_grouping:
        items = group_similar(items)

    # log.info(items)

    tmpl = template_lookup.get_template("multi_selector.mako")
    output = tmpl.render(
        field_name=field_name,
        items=items,
        ignore_prefix=ignore_prefix)

    if PY3:
        output = output.decode('utf-8')

    return output
