"""
This extension lists my custom Albert plugins with their shortcut and what each one does.
"""

import ast
from dataclasses import dataclass
from pathlib import Path

from albert import *

md_iid = "5.0"
md_version = "1.1"
md_name = "My Shortcuts"
md_description = "List my custom plugins, their shortcuts and what they do"
md_license = "BSD-2"
md_url = "https://github.com/ibrahimalkurdi/albert-todo-plugin"
md_authors = ["@ibrahimalkurdi"]
md_maintainers = ["@ibrahimalkurdi"]

PLUGINS_DIR = Path(__file__).parent.parent


@dataclass
class Shortcut:
    trigger: str
    name: str
    description: str
    usage: str


def _returned_string(node: ast.FunctionDef) -> str:
    for stmt in ast.walk(node):
        if isinstance(stmt, ast.Return) and isinstance(stmt.value, ast.Constant) and isinstance(stmt.value.value, str):
            return stmt.value.value
    return ""


def read_shortcut(init_file: Path) -> Shortcut | None:
    try:
        tree = ast.parse(init_file.read_text())
    except (OSError, SyntaxError) as e:
        warning(f"{init_file}: {e}")
        return None
    meta: dict[str, str] = {}
    methods: dict[str, str] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    meta[target.id] = node.value.value
        elif isinstance(node, ast.FunctionDef) and node.name in ("defaultTrigger", "synopsis"):
            methods[node.name] = _returned_string(node)
    trigger = methods.get("defaultTrigger")
    if not trigger:
        return None
    return Shortcut(
        trigger=trigger,
        name=meta.get("md_name", init_file.parent.name),
        description=meta.get("md_description", ""),
        usage=methods.get("synopsis", ""),
    )


def load_shortcuts() -> list[Shortcut]:
    own = Path(__file__).resolve()
    shortcuts = []
    for init_file in sorted(PLUGINS_DIR.glob("*/__init__.py")):
        if init_file.resolve() == own:
            continue
        if shortcut := read_shortcut(init_file):
            shortcuts.append(shortcut)
    return shortcuts


class Plugin(PluginInstance, GeneratorQueryHandler):

    def __init__(self):
        PluginInstance.__init__(self)
        GeneratorQueryHandler.__init__(self)

    def defaultTrigger(self):
        return "help "

    def synopsis(self, query):
        return "<filter>"

    def items(self, ctx):
        needle = ctx.query.strip().lower()
        items = []
        for s in load_shortcuts():
            if needle and needle not in f"{s.trigger} {s.name} {s.description}".lower():
                continue
            command = f"{s.trigger}{s.usage}".strip()
            items.append(StandardItem(
                id=f"{self.id()}.{s.trigger.strip()}",
                text=f"{command}  —  {s.name}",
                subtext=s.description,
                icon_factory=lambda: Icon.grapheme("❔"),
                actions=[
                    Action("open", "Open this plugin", lambda t=s.trigger: runDetachedProcess(["albert", "show", t])),
                    Action("copy", "Copy shortcut", lambda t=s.trigger: setClipboardText(t)),
                ],
            ))
        if items:
            yield items
