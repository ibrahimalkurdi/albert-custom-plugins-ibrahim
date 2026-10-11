"""
This extension show my todo list.
"""

from pathlib import Path

from albert import *

md_iid = "5.0"
md_version = "1.0"
md_name = "My List"
md_description = "Show my todo list in a popup screen"
md_license = "BSD-2"
md_url = "https://github.com/ibrahimalkurdi/albert-todo-plugin"
md_authors = ["@ibrahimalkurdi"]
md_maintainers = ["@ibrahimalkurdi"]

SCRIPT = str(Path.home() / "scripts" / "show-up-my-todo-list.sh")


class Plugin(PluginInstance, GeneratorQueryHandler):

    def __init__(self):
        PluginInstance.__init__(self)
        GeneratorQueryHandler.__init__(self)

    def defaultTrigger(self):
        return "mylist "

    def items(self, ctx):
        yield [
            StandardItem(
                id=self.id(),
                text="My todo list",
                subtext="Show my todo list",
                icon_factory=lambda: Icon.grapheme("📋"),
                actions=[Action("run", "Run script", lambda: runDetachedProcess(["bash", SCRIPT]))],
            )
        ]
