"""
This extension provides a quick run for my todo script and passing the TODO new item from Albert application launcher.
"""

from pathlib import Path

from albert import *

md_iid = "5.0"
md_version = "1.0"
md_name = "TODO List"
md_description = "Automated task addition to my TODO list file"
md_license = "BSD-2"
md_url = "https://github.com/ibrahimalkurdi/albert-todo-plugin"
md_authors = ["@ibrahimalkurdi"]
md_maintainers = ["@ibrahimalkurdi"]

SCRIPT = str(Path.home() / "scripts" / "automated_todo_list.sh")


class Plugin(PluginInstance, GeneratorQueryHandler):

    def __init__(self):
        PluginInstance.__init__(self)
        GeneratorQueryHandler.__init__(self)

    def defaultTrigger(self):
        return "todo "

    def synopsis(self, query):
        return "<Add your Todo list item>"

    def items(self, ctx):
        task = ctx.query.strip()
        if not task:
            return
        yield [
            StandardItem(
                id=self.id(),
                text=f"Add task: {task}",
                subtext="Each entry will add single task to the automated TODO list",
                icon_factory=lambda: Icon.grapheme("✅"),
                actions=[Action("run", "Add task", lambda t=task: runDetachedProcess(["bash", SCRIPT, t]))],
            )
        ]
