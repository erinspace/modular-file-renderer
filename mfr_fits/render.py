''' FITS renderer module!
'''

import os

from mfr import config as core_config

from mfr.core import RenderResult, get_assets_from_list


JS_ASSETS = [
    "js9support.min.js",
    "js9plugins.js",
    "js9.min.js",
    "fitsy.min.js"
]

CSS_ASSETS = [
    "js9.css",
    "js9support.css"
]

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, 'templates', 'fits.html')


def render_html(fp, src=None, **kwargs):

    src = src or fp.name

    with open(TEMPLATE) as template:
        content = template.read().format(fits_file=  '\'' + src + '\'')

    assets_uri_base = '{0}/mfr_fits'.format(core_config['STATIC_URL'])

    assets = {
        'js': get_assets_from_list(assets_uri_base, 'js', JS_ASSETS),
        'css': get_assets_from_list(assets_uri_base, 'css', CSS_ASSETS)
    }

    return RenderResult(content, assets)




