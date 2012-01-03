import os
import sys

import optparse

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

#import importlib
#from ..apps import enabled_apps

from pyramid.scaffolds import Template
from pyramid.scripts.pcreate import PCreateCommand

class TempCommand(object):
    parser = optparse.OptionParser()
    parser.add_option('--simulate',
                      dest='simulate',
                      action='store_true',
                      help='Simulate but do no work')
    
    parser.add_option('--interactive',
                      dest='interactive',
                      action='store_true',
                      help='When a file would be overwritten, interrogate')

    def __init__(self):
        self.options, self.args = self.parser.parse_args()
        self.verbosity=1

    

class NewAppTemplate(Template):
    _template_dir = 'newapp_scaffold'
    summary = 'New sub-application creation script'
    
    def post(self, command, output_dir, vars): # pragma: no cover
        val = Template.post(self, command, output_dir, vars)
        self.out('')
        self.out('Your application has been created under apps/%s' % vars['appname'])
        return val

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <application_name>\n'
          '(example: "%s myapp2")' % (cmd, cmd)) 
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    
    new_appname = sys.argv[1]
    here_parent = os.path.dirname(os.path.dirname(__file__))
    apps_path = here_parent+'/apps'
    #sys.path.insert(0, here_parent+'/apps')
    #sys.path.insert(0, here_parent)
    print("creating %s" % new_appname)
    
    #command = TempCommand()
    command = PCreateCommand(argv)
        
    app_creator = NewAppTemplate('newapp')
    app_creator.run(command, apps_path + '/' + new_appname,
                    {'appname': new_appname})
    