import datetime

AUTHOR = 'WeBuyTCGCards.com'
SITENAME = 'WeBuyTCGCards.com'
SITEURL = ""

PATH = "content"
OUTPUT_PATH = "output"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

JINJA_GLOBALS = {'now': datetime.datetime.now()}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Pretty URLs for pages (no /pages/ prefix)
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Navigation menu
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ("Home", "/"),
    ("Sell", "/sell/"),
    ("Buylist", "https://buylist.sortswift.com/?s=f5ab4e224feb1f93"),
    ("Contact", "/contact/"),
    ("About", "/about/"),
)

# Static assets
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
}

# Theme
THEME = "themes/navy-modern"

