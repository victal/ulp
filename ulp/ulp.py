#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urwid

from widgets.link import Link
from widgets.listbox import WrappingListBox

choices = [
    "http://xkcd.org",
    "http://g1.com.br",
    "http://google.com"
]

selected = []


def toggle_selection(link):
    if link in selected:
        selected.remove(link)
    else:
        selected.append(link)


def menu(choices):
    body = []
    for c in choices:
        button = Link(c, toggle_selection)

        body.append(urwid.AttrMap(button, None, focus_map={'selected': 'focus_selected', 'unselected': 'focused'}))
    return WrappingListBox(urwid.SimpleFocusListWalker(body))

def exit_program(button):
    raise urwid.ExitMainLoop()

def get_help_text():
    commands = {
            'c': 'Copy to clipboard',
            'Enter': 'Open in browser',
            'x': 'Command mode',
            'Space': 'Select'
    }
    text = ''
    for key, value in commands.iteritems():
        text += "[{}]: {}".format(key, value) + "    "
    
    return urwid.Pile([
        urwid.Divider(u"="),
        urwid.Text(unicode(text))
    ])
palette = [
    ('focus_selected', 'white', 'dark red'),
    ('focused', 'light gray', 'dark blue'),
    ('selected', 'white', 'light green'),
    ('unselected', 'black', '')
]
main_menu = urwid.Padding(menu(choices), left=0, right=0)
help_text = get_help_text()
main = urwid.Frame(main_menu, footer=help_text)
urwid.MainLoop(main, palette=palette, unhandled_input=exit_program).run()
