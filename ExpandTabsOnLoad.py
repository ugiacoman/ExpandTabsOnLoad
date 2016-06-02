import os
import re
import sublime
import sublime_plugin


class ExpandTabsOnLoad(sublime_plugin.EventListener):
    def on_load(self, view):
        view.run_command('expand_tabs', {"set_translate_tabs": True})
