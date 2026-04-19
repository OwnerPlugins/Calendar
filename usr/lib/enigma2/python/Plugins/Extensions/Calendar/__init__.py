#!/usr/bin/python
# -*- coding: utf-8 -*-


import gettext

from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from Components.Language import language

"""
###########################################################
#  Calendar Planner for Enigma2 v1.9                      #
#  Created by: Lululla                                    #
###########################################################

Last Updated: 2026-01-15
Status: Stable with complete vCard & ICS support
Credits: Lululla
Homepage: www.corvoboys.org www.linuxsat-support.com
###########################################################
"""

PLUGIN_NAME = "Calendar"
__version__ = "2.1"

PLUGIN_PATH = resolveFilename(
    SCOPE_PLUGINS,
    "Extensions/{}".format(PLUGIN_NAME))
PLUGIN_ICON = resolveFilename(SCOPE_PLUGINS, "Extensions/Calendar/plugin.png")
USER_AGENT = "Calendar-Enigma2-Updater/%s" % __version__
PluginLanguageDomain = 'Calendar'
PluginLanguagePath = "Extensions/Calendar/locale"


def localeInit():
    if PLUGIN_NAME and PluginLanguagePath:
        gettext.bindtextdomain(
            PluginLanguageDomain,
            resolveFilename(
                SCOPE_PLUGINS,
                PluginLanguagePath))


def _(txt):
    translated = gettext.dgettext(PluginLanguageDomain, txt)
    if translated:
        return translated
    else:
        print(("[%s] fallback to default translation for %s" %
              (PluginLanguageDomain, txt)))
        return gettext.gettext(txt)


localeInit()
language.addCallback(localeInit)
