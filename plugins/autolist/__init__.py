"""
This extension show automated todo list.
"""

from albert import *
import subprocess
import sys

md_iid = "0.5"
md_version = "0.1"
#md_id = ""
md_name = "Automated todo List"
md_description = "Show automated todo list in a popup screen"
md_license = "BSD-2"
md_url = "https://github.com/ibrahimalkurdi/albert-todo-plugin"
md_maintainers = "@ibrahimalkurdi"

class Plugin(QueryHandler):
    def id(self):
        return md_id

    def name(self):
        return md_name

    def description(self):
        return md_description

    def initialize(self):
        info('initialize')

    def finalize(self):
        info('finalize')

    #def synopsis(self):
    #    return '[[Show my todo list]]'

    def handleQuery(self, query):
        #if query.string.strip():
        #    args = query.string.strip()
        query.add(Item(
            id="Id",
            #text="Task list show up",
            #subtext="Each entry will add single task to the automated TODO list",
            actions=[Action('Run script', 'Run Script', lambda: subprocess.Popen(['bash', '/home/ibrahim/scripts/show-up-automated-todo-list.sh' ]) )]
        ))
