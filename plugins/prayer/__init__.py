from pathlib import Path

from albert import *

md_iid = "5.0"
md_version = "2.0"
md_name = "Prayer Website"
md_description = "Opens the prayer static website"
md_license = "BSD-2"
md_url = "https://alsakina.pages.dev"
md_authors = ["@ibrahimalkurdi"]
md_maintainers = ["@ibrahimalkurdi"]

ICON_PATH = Path(__file__).parent / "prayer.svg"
WEBSITE_URL = "https://alsakina.pages.dev"


class Plugin(PluginInstance, GeneratorQueryHandler):

    def __init__(self):
        PluginInstance.__init__(self)
        GeneratorQueryHandler.__init__(self)

    def defaultTrigger(self):
        return "prayer"

    def items(self, ctx):
        yield [
            StandardItem(
                id=self.id(),
                text="Open static website",
                subtext=WEBSITE_URL,
                icon_factory=lambda: Icon.image(ICON_PATH),
                actions=[Action("open", "Open in browser", lambda: openUrl(WEBSITE_URL))],
            )
        ]
