# -*- coding: utf-8 -*-

from flask.ext.assets import Bundle, Environment

JS_ASSETS = [
    'js/jquery-1.9.1.js',
    'js/jquery.tablesorter.js',
    'js/bootstrap.js'
]
JS_TIMELINE_ASSETS = [
    'js/timeline.js',
    'js/eventviz-timeline.js'
]
CSS_ASSETS = [
    'css/bootstrap.css',
    'css/bootstrap-responsive.css',
    'css/eventviz.css'
]
CSS_TIMELINE_ASSETS = [
    'css/timeline.css'
]
JS_MINIFIER = 'yui_js'
CSS_MINIFIER = 'yui_css'


def setup_assets(app):
    assets = Environment(app)

    js_all = Bundle(*JS_ASSETS, filters=JS_MINIFIER, output='js/eventviz.min.js')
    assets.register('js_all', js_all)

    js_timeline = Bundle(*JS_TIMELINE_ASSETS, filters=JS_MINIFIER, output='js/timeline.min.js')
    assets.register('js_timeline', js_timeline)

    css_all = Bundle(*CSS_ASSETS, filters=CSS_MINIFIER, output='css/eventviz.min.css')
    assets.register('css_all', css_all)

    css_timeline = Bundle(*CSS_TIMELINE_ASSETS, filters=CSS_MINIFIER, output='css/timeline.min.css')
    assets.register('css_timeline', css_timeline)
