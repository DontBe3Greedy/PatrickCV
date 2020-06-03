"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle
from scss import Compiler
from scss.namespace import Namespace

namespace = Namespace()
compiler = Compiler(namespace=namespace)


# Namespace variables


def pyscss_filter(_in, out, **kw):
    """
    Custom pyscss filter, I forgot why, but I know its needed
    :param _in: Input stream that reads the scss file
    :param out: Out stream that writes to the css file
    :param kw:
    :return:
    """
    out.write(compiler.compile_string(_in.read()))


def compile_static_assets(assets):
    """
    Create stylesheet bundles.
    :param assets: Flask-Assets Environment
    :type assets: Environment
    """
    assets.auto_build = True
    assets.debug = True
    common_scss_bundle = Bundle('source/scss/*.scss',
                                filters=(pyscss_filter, 'cssmin'),
                                output='dist/css/style.min.css',
                                extra={'rel': 'stylesheet/scss'})
    home_scss_bundle = Bundle('home_bp/scss/*.scss',
                              filters=(pyscss_filter, 'cssmin'),
                              output='dist/css/home.min.css',
                              extra={'rel': 'stylesheet/scss'})
    home_js_bundle = Bundle('home_bp/js/events.js',
                            filters="jsmin",
                            output="dist/js/home.min.js")

    assets.register('common_scss_bundle', common_scss_bundle)
    assets.register('home_scss_bundle', home_scss_bundle)
    assets.register('home_js_bundle', home_js_bundle)

    if app.config['FLASK_ENV'] == 'development':  # Only rebuild bundles in development
        common_scss_bundle.build()
        home_scss_bundle.build()
        home_js_bundle.build()
        home_scss_bundle.debug = True

    return assets
