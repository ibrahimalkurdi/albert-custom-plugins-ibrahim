from pathlib import Path
from albert import Action, Item, Query, QueryHandler, openUrl

# ─── Metadata ───────────────────────────────────────────────────────
md_iid = "0.5"
md_version = "1.0"
md_name = "Static Website"
md_description = "Opens a static website"
md_url = "https://example.com"
md_maintainers = "@you"

ICON_PATH = str(Path(__file__).parent / "prayer.svg")  # optional icon file
WEBSITE_URL = "https://dump-767d2.web.app"                     # <- put your site here


# ─── Plugin Class ───────────────────────────────────────────────────
class Plugin(QueryHandler):

    def id(self) -> str:
        return __name__

    def name(self) -> str:
        return md_name

    def description(self) -> str:
        return md_description

    def defaultTrigger(self) -> str:
        return "prayer"             # type "site" in Albert to trigger it

    def synopsis(self) -> str:
        return ""                  # no search text needed

    def handleQuery(self, query: Query) -> None:
        # Ignore any extra text, just offer to open the static site
        item = Item(
            id=f"{md_name}/open",
            text="Open static website",
            subtext=WEBSITE_URL,
            icon=[ICON_PATH],
            actions=[
                Action(f"{md_name}/open", "Open in browser", lambda: openUrl(WEBSITE_URL))
            ],
        )
        query.add(item)

