"""
This extension provides a quick run for my todo script and passing the TODO new item from Albert pop up window.
"""

from albert import *
import subprocess
import sys

md_iid = "0.5"
md_version = "1.2"
#md_id = "overwrite"
md_name = "TDOD script"
md_description = "TDOD addition tasks to my automated TODO file"
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

    def handleQuery(self, query):
        if query.string.strip():
            args = query.string.strip()
        query.add(Item(
            id="Id",
            text="Text",
            subtext="Subtext",
            actions=[Action('Run script', 'Run Script', lambda: subprocess.Popen(['bash', '~/automated_todo_list.sh', args  ]) )]
        ))
