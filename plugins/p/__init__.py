"""
This extension help to autocomplete python custom plugins
"""

from albert import *
import subprocess
import sys

md_iid = "0.5"
md_version = "0.2"
#md_id = "vs"
md_name = "Autocomplete Python Plugin"
md_description = "Help to do command completion for Python Custom Plugin"
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
        command_mapping = {
            "vs": "vsrepo ",
            "my": "mylist ",
            "to": "todo ",
            "au": "autolist ",
            # Add more mappings as needed
        }
        partial_command = query.string.lower()

        if partial_command in command_mapping:
            full_command = command_mapping[partial_command]
            query.add(Item(
                id="Id",
                text="Python Plugin Autocompletion",
                subtext="provide a couple of letter from the command that you want to auto-complete",
                completion=full_command,
        ))
