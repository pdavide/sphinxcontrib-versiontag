"""Sphinx extension that retrieves project versions."""

from __future__ import print_function

import os, urllib, json

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.errors import ExtensionError, SphinxError

__author__ = 'Team per la Trasformazione Digitale'
__license__ = 'BSD-3-clause'
__version__ = '0.0.1'

def setup(app):
    """Called by Sphinx during phase 0 (initialization).

    :param app: Sphinx application object.

    :returns: Extension version.
    :rtype: dict
    """
    app.connect('html-page-context', add_last_stable_version)
    return {'version': __version__}

def add_last_stable_version(app, pagename, templatename, ctx, event_arg):
    """Called when the HTML builder has created a context dictionary to render a template with.

    If on RTD add 'last_stable_version' variable to context

    :param sphinx.application.Sphinx app: Sphinx application object.
    :param str pagename: Name of the page being rendered (without .html or any file extension).
    :param str templatename: Page name with .html.
    :param dict context: Jinja2 HTML context.
    :param docutils.nodes.document doctree: Tree of docutils nodes.
    """
    on_rtd = os.environ.get('READTHEDOCS') == 'True'
    if on_rtd and app.builder.name == 'readthedocs':
        url = 'http://readthedocs.org/api/v1/version/%s/?format=json' % (ctx['slug'])
        versions = {}
        stable_identifier = None
        while True:
            response = urllib.urlopen(url)
            data = json.load(response)
            for version in data['objects']:
                if version['slug'] != 'stable':
                    versions[version['identifier']] = version['slug']
                else:
                    stable_identifier = version['identifier']
                if stable_identifier in versions:
                    ctx['last_stable_version'] = versions[stable_identifier]
                    return
            if data['meta']['next'] != None:
                url = 'http://readthedocs.org' + data['meta']['next']
            else:
                break
