import wtforms
from mako.template import Template

from template_lookup import template_lookup

class Form(wtforms.Form):
    """
    The Form base class, extends from WTForms.Form
    
    This class provides some additional features to the base wtforms.Form class. These include:
    
    * Methods to render the form in HTML
        * as_p to render form using p tags
        * TODO: as_table to render using html table
        * TODO: as_div to render using html divs
    
    * TODO: CSRF protection availability
    """
    
    def __init__(self, formdata=None, obj=None, prefix='', **kwargs):
        
        super(Form, self).__init__(formdata, obj, prefix, **kwargs)
        #wtforms.Form.__init__(self, formdata=None, obj=None, prefix='', **kwargs)
    
    def as_p(self, labels='top', errors='right'):
        """
        Output each form field as html **p** tags. By default labels are displayed on top of the form fields
        and validation erros are displayed on the right of the form fields. Both these behaviors can be
        changed by settings values for the labels and errors parameters.
        
        Values can be left, top, right or bottom
        
        """
        
        tmpl = template_lookup.get_template("form_as_p.mako")
        
        return tmpl.render(form=self, labels_position=labels.lower(), errors_position=errors.lower())



