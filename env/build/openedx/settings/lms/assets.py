"""
Bare minimum settings for collecting production assets.
"""
from ..common import *
from openedx.core.lib.derived import derive_settings

ENABLE_COMPREHENSIVE_THEMING = True
COMPREHENSIVE_THEME_DIRS.append('/openedx/themes')

STATIC_ROOT_BASE = '/openedx/staticfiles'

SECRET_KEY = 'secret'
XQUEUE_INTERFACE = {
    'django_auth': None,
    'url': None,
}
DATABASES = {
    "default": {},
}



STATIC_ROOT = path(STATIC_ROOT_BASE)
WEBPACK_LOADER['DEFAULT']['STATS_FILE'] = STATIC_ROOT / "webpack-stats.json"

derive_settings(__name__)

LOCALE_PATHS.append("/openedx/locale/contrib/locale")
LOCALE_PATHS.append("/openedx/locale/user/locale")