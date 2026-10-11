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
DEFAULT_URL = "https://alsakina.pages.dev"


class Plugin(PluginInstance, GeneratorQueryHandler):

    def __init__(self):
        PluginInstance.__init__(self)
        GeneratorQueryHandler.__init__(self)
        self._url = self.readConfig("url", str) or DEFAULT_URL

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str):
        self._url = value.strip() or DEFAULT_URL
        self.writeConfig("url", self._url)

    def configWidget(self):
        return [
            {
                "type": "lineedit",
                "property": "url",
                "label": "Website URL",
            }
        ]

    def defaultTrigger(self):
        return "prayer"

    def items(self, ctx):
        url = self._url
        yield [
            StandardItem(
                id=self.id(),
                text="Open static website",
                subtext=url,
                icon_factory=lambda: Icon.image(ICON_PATH),
                actions=[Action("open", "Open in browser", lambda: openUrl(url))],
            )
        ]
