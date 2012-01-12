import wtforms
from mako.template import Template

from template_lookup import template_lookup

class Form(wtforms.Form):
    """
    The Form base class, extends from WTForms.Form
    
    This class provides some additional features to the base wtforms.Form class. These include:
    
    * Methods to render the form in HTML
        * as_p to render form using p tags
        * as_table to render using html table
    
    * CSRF protection availability 
    
    * TODO: Since WTForms wants presentation attributes (like rows and cols for textarea) to be set on
    instantiated form instances (not the class itself), allow some way to specify field attributes
    that are then read at field display time. Possibly a field_attrs dict??? May be reimplementing sub-classes of some fields to make use of it would be a could idea??
    
    """
    
    def __init__(self, formdata=None, obj=None, prefix='', request_obj=None, use_csrf_protection=False, **kwargs):
        
        super(Form, self).__init__(formdata, obj, prefix, **kwargs)
        
        self._use_csrf_protection = use_csrf_protection
        if use_csrf_protection:
            if request_obj is None:
                raise Exception("Cannot use CSRF protection without a request object being passed to the form")
            else:
                self._request = request_obj
                self._csrf_token = self._request.session.get_csrf_token()
            
        #wtforms.Form.__init__(self, formdata=None, obj=None, prefix='', **kwargs)
    
    def validate(self):
        """
        Validate form fields and check for CSRF token match if use_csrf_protection was set to true when
        initializing the form.
        """
        
        validate_result = super(Form, self).validate()
        
        if validate_result:
            # now verify the csrf token if using csrf protection
            if self._use_csrf_protection:
                if self._csrf_token != self._request.params['csrf_token']:
                    self.errors['_csrf'] = ['CSRF token did not match',]
                    return False
        
        return validate_result
        
    def as_p(self, labels='top', errors='right'):
        """
        Output each form field as html **p** tags. By default labels are displayed on top of the form fields
        and validation erros are displayed on the right of the form fields. Both these behaviors can be
        changed by settings values for the labels and errors parameters.
        
        Values can be left, top, right or bottom
        
        """
        
        tmpl = template_lookup.get_template("form_as_p.mako")
        
        return tmpl.render(form=self, labels_position=labels.lower(), errors_position=errors.lower())
    
    def as_table(self, labels='left', errors='top', include_table_tag=False):
        """
        Output the form as HTML Table, optionally add the table tags too if include_table_tag is set to True (default False)
        """
        
        tmpl = template_lookup.get_template("form_as_table.mako")
        
        return tmpl.render(form=self, labels_position=labels.lower(), errors_position=errors.lower(), include_table_tag=include_table_tag)



