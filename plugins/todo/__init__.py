"""
This extension provides a quick run for my todo script and passing the TODO new item from Albert application launcher.
"""

from albert import *
import subprocess
import sys

md_iid = "0.5"
md_version = "0.2"
#md_id = "overwrite"
md_name = "TODO List"
md_description = "Automated task addition to my TODO list file"
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

    def synopsis(self):
        return '[[Add your Todo list item]]'

    def handleQuery(self, query):
        if not query.isValid:
            return
        if query.string.strip():
            args = query.string.strip()
        query.add(Item(
            id="Id",
            text="Task Management",
            subtext="Each entry will add single task to the automated TODO list",
            actions=[Action('Run script', 'Run Script', lambda: subprocess.Popen(['bash', '/home/ibrahim/scripts/automated_todo_list.sh', args  ]) )]
        ))
