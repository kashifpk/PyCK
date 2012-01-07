.. _pyck-forms:

The pyck.forms Package
======================

.. automodule:: pyck.forms
    :members:

Here is an example usage to demonstrate the improvements::
    
    from pyck.forms import Form
    from wtforms import TextField, validators
    class MyForm(Form):
        name = TextField("Name", [validators.required()])
        fname = TextField("Father's Name", [validators.required()])
    
    myform = MyForm()
    str(myform.as_p())
    r'\n<p>\n<label for="name">Name</label><br /> <input id="name" name="name" type="text" value="" /> </p>\n\n<p>\n<label for="fname">Father\'s Name</label><br /> <input id="fname" name="fname" type="text" value="" /> </p>\n'
    myform.validate()
    False
    str(myform.as_p(labels='left', errors='right'))
    '\n<p>\n<label for="name">Name</label> <input id="name" name="name" type="text" value="" /> <span class="errors">This field is required.</span> </p>\n\n<p>\n<label for="fname">Father\'s Name</label> <input id="fname" name="fname" type="text" value="" /> <span class="errors">This field is required.</span> </p>\n'

Within a template, all you need to do is to just call the form's rendering function, for example::

    ${myform.as_p() | n}

