from pyramid.scaffolds import PyramidTemplate
from pyramid.scaffolds.template import Template
import os, zipfile


class PyCKTemplate(PyramidTemplate):
    _template_dir = 'template'
    summary = 'PyCK based web application'

    def post(self, command, output_dir, vars): # pragma: no cover
        """ Overrides :meth:`pyramid.scaffold.template.Template.post`, to
        print "Welcome to Pyramid.  Sorry for the convenience." after a
        successful scaffolding rendering."""
        
        # Unzip the projectname/scripts/newapp_scaffold.zip
        self.out('\n  Extracting the new app creation templates\n')
        pkg_name = vars['package']
        
        extract_path = "%s/%s/scripts/" % (pkg_name, pkg_name)
        zipfilepath = "%s/newapp_scaffold.zip" % extract_path
        
        z = zipfile.ZipFile(zipfilepath)
        z.extractall(extract_path)
        
        os.unlink(zipfilepath)
        
        self.out('Welcome to PyCK.  Sorry for the convenience :-)')
        return Template.post(self, command, output_dir, vars)