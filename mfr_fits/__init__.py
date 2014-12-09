from mfr.core import FileHandler, get_file_extension
from mfr_fits.render import render_html

EXTENSIONS = [
    '.fits',
    '.FITS'
]


class Handler(FileHandler):
    """The fits file handler"""

    renderers = {
        'html': render_html
    }

    def detect(self, fp):
        return get_file_extension(fp.name) in EXTENSIONS
