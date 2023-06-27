"""
This extension help to open a single Git repo in a new Visual Studio Code window.
"""

from albert import *
import subprocess
import sys

md_iid = "0.5"
md_version = "0.2"
#md_id = "vs"
md_name = "Visual Studio Code Git Repo"
md_description = "Pick up a Repo and open it in Visual Studio"
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
        query.add(Item(
            id="Id",
            text="VS code Repo",
            subtext="Pick up a Git Repo from a List and open it in VS code",
            actions=[Action('Run script', 'Run Script', lambda: subprocess.Popen(['gnome-terminal', '--', 'sh', '-c', '/home/ibrahim/scripts/vs-code-pick-up-repo.sh | bash' ]) )]
        ))
