from wtforms import Form as WTForm

class Form(WTForm):
    """
    The Form base class, extends from WTForms.Form
    
    This class provides some additional features to the base wtforms.Form class. These include:
    
    * Methods to render the form in HTML
    
    * CSRF protection availability
    """
    
    def __init__(self, formdata=None, obj=None, prefix='', **kwargs):
        
        super(Form, self).__init__(formdata=None, obj=None, prefix='', **kwargs)
    
    def as_p(self, labels='top', errors='right'):
        """
        Output each form field as html **p** tags. By default labels are displayed on top of the form fields and validation erros are displayed on the right of the form fields. Both these behaviors can be changed by settings values for the labels and errors parameters.
        """
        
        for field in self:
            print(field.name)



