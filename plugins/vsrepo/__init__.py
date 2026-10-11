"""
This extension help to open a single Git repo in a new Visual Studio Code window.
"""

from pathlib import Path

from albert import *

md_iid = "5.0"
md_version = "1.0"
md_name = "Visual Studio Code Git Repo"
md_description = "Pick up a Repo and open it in Visual Studio"
md_license = "BSD-2"
md_url = "https://github.com/ibrahimalkurdi/albert-todo-plugin"
md_authors = ["@ibrahimalkurdi"]
md_maintainers = ["@ibrahimalkurdi"]

SCRIPT = str(Path.home() / "scripts" / "vs-code-pick-up-repo.sh")


class Plugin(PluginInstance, GeneratorQueryHandler):

    def __init__(self):
        PluginInstance.__init__(self)
        GeneratorQueryHandler.__init__(self)

    def defaultTrigger(self):
        return "vsrepo "

    def items(self, ctx):
        yield [
            StandardItem(
                id=self.id(),
                text="VS code Repo",
                subtext="Pick up a Git Repo from a List and open it in VS code",
                icon_factory=lambda: Icon.grapheme("🗂️"),
                actions=[Action(
                    "run",
                    "Run script",
                    lambda: runDetachedProcess(["gnome-terminal", "--", "sh", "-c", f"{SCRIPT} | bash"]),
                )],
            )
        ]
