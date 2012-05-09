import os
from mako.lookup import TemplateLookup

here = os.path.dirname(__file__)
template_lookup = TemplateLookup(directories=[here+'/templates'],
                                 module_directory=here+'/cache',
                                 output_encoding='utf8',
                                 input_encoding='utf8',
                                 encoding_errors='ignore')

