"""
Utility code related to url manipulation and handling
"""

def split_query_string(query_string):
    """
    Splits a query string into a dictionary

    >>> split_query_string('a=1&b=2&name=abc&y=&z=ab23')
    {'a': '1', 'y': '', 'b': '2', 'name': 'abc', 'z': 'ab23'}
    """

    qs_dict = {}
    qs_parts = query_string.split('&')

    for qs_part in qs_parts:
        k,v = qs_part.split('=')
        qs_dict[k] = v

    return qs_dict


def join_query_string(qs_dict):
    """
    Joins query string from a dictionary
    
    >>> join_query_string({'a': '1', 'y': '', 'b': '2', 'name': 'abc', 'z': 'ab23'})
    'a=1&y=&b=2&name=abc&z=ab23'
    """

    parts = []
    for k,v in qs_dict.items():
        parts.append("{}={}".format(k, v))

    return "&".join(parts)


def url_without(url, **kwargs):
    """
    Return the url stripping the given section off the url
    
    examples:
    >>> url_without('http://acme.org/abc', qs='page')
    'http://acme.org/abc'
    >>> url_without('http://acme.org/abc?page=1', qs='page')
    'http://acme.org/abc'
    >>> url_without('http://acme.org/abc?a=b&page=1', qs='page')
    'http://acme.org/abc?a=b'
    >>> url_without('http://acme.org/abc?a=b&page=1&c=d', qs='page')
    'http://acme.org/abc?a=b&c=d'
    >>> url_without('http://acme.org/abc?a=b&page=1&c=d', qs=['page', 'c'])
    'http://acme.org/abc?a=b'
    """

    if 'qs' in kwargs:
        qs = kwargs['qs']

        # return the url unchanged if it doesn't contain query string
        if '?' not in url:  
            return url

        new_url, url_qs = url.split('?')
        qs_dict = split_query_string(url_qs)

        if type(qs) not in (tuple, list):
            qs = [qs,]

        for qs_item in qs:
            if qs_item in qs_dict:
                del qs_dict[qs_item]
        
        url_qs = join_query_string(qs_dict)
        if url_qs:
            return new_url + '?' + url_qs
        else:
            return new_url

    return url


def url_add(url, **kwargs):
    """
    Return the url adding the given section into the url
    
    examples:
    >>> url_add('http://acme.org/abc', qs='page=4')
    'http://acme.org/abc?page=4'
    >>> url_add('http://acme.org/abc?page=1', qs='name=xyz')
    'http://acme.org/abc?page=1&name=xyz'
    >>> url_add('http://acme.org/abc?a=b&page=1', qs='name=xyz')
    'http://acme.org/abc?a=b&page=1&name=xyz'
    >>> url_add('http://acme.org/abc?a=b', qs=['page=1', 'c=d'])
    'http://acme.org/abc?a=b&page=1&c=d'
    """

    if 'qs' in kwargs:
        qs = kwargs['qs']
        if type(qs) not in (tuple, list):
            qs = [qs,]

        if '?' not in url:  
            return url + '?' + "&".join(qs)
        else:
            return url + '&' + "&".join(qs)

    return url
