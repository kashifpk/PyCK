from pyramid.scaffolds import PyramidTemplate
from pyramid.scaffolds.template import Template

class PyCKTemplate(PyramidTemplate):
    _template_dir = 'template'
    summary = 'PyCK based web application'

    def post(self, command, output_dir, vars): # pragma: no cover
        """ Overrides :meth:`pyramid.scaffold.template.Template.post`, to
        print "Welcome to Pyramid.  Sorry for the convenience." after a
        successful scaffolding rendering."""
        self.out('Welcome to PyCK.  Sorry for the convenience :-)')
        return Template.post(self, command, output_dir, vars)