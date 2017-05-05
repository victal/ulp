#!/usr/bin/env python
# coding=utf-8
import os
import sys
import subprocess

import urwid

from ulp.widgets.link import Link, do_nothing
from ulp.widgets.listbox import WrappingListBox
from ulp.widgets.popup import PopUpDialog, PopUpWrapper
import pyperclip


def exit_program(key):
    raise urwid.ExitMainLoop()


PALETTE = [
    ('focus_selected', 'white', 'dark red'),
    ('focused', 'light gray', 'dark blue'),
    ('selected', 'white', 'light green'),
    ('unselected', 'black', ''),
    ('popup', 'light gray', 'black')
]

COMMANDS = [
    ('c', 'Copy to clipboard'),
    ('Enter', 'Open in browser'),
    ('x', 'Command mode'),
    ('Space', 'Select'),
    ('q', 'Exit')
]

class ClickableLink(Link):

    def __init__(self, link, on_select=do_nothing, align='left', wrap='space'):
        Link.__init__(self, link=link, on_select=on_select, align=align, wrap=wrap)

    def mouse_event(self, size, event, button, col, row, focus):
        if event == "mouse press":
            self._toggle_selection()
        return True


class Interface(urwid.Frame):

    def __init__(self, choices):
        super(Interface, self).__init__(self._create_body(choices), footer=Interface._get_help_text())
        self._selected = []
        self._total_choices = len(choices)

    def keypress(self, size, key):
        if key == 'c':
            self._copy_selected_to_clipboard()
            return
        elif key == 'enter':
            self._open_links()
            exit_program(key);
        elif key == 'q':
            exit_program(key);

        urwid.Frame.keypress(self, size, key)
        return key in [cmd[0] for cmd in COMMANDS]

    def mouse_event(self, size, event, button, col, row, focus):
        urwid.Frame.mouse_event(self, size, event, button, col, row, focus)
        return True

    def toggle_selection(self, link):
        if link in self._selected:
            self._selected.remove(link)
        else:
            self._selected.append(link)
    
    def _copy_selected_to_clipboard(self):
        try:
            pyperclip.copy(os.linesep.join(self._selected))
        except pyperclip.exceptions.PyperclipException as e:
            self._body.create_popup(urwid.Text(str(e)))
            

    def _create_body(self, choices):
        body = []
        for c in choices:
            button = ClickableLink(c, self.toggle_selection)

            body.append(
                urwid.AttrMap(button, None, focus_map={'selected': 'focus_selected', 'unselected': 'focused'}))
        return PopUpWrapper(WrappingListBox(urwid.SimpleFocusListWalker(body)))

    @classmethod
    def _get_help_text(cls):
        text = ''
        for key, value in COMMANDS:
            text += "[{}]: {}".format(key, value) + "    "

        return urwid.Pile([
            urwid.Divider("="),
            urwid.Text(text)
        ])

    def _open_links(self):
        if not self._selected:
            # Open link under cursor
            attrmap = self.focus.original_widget.focus 
            link = attrmap.original_widget.get_link()
            subprocess.call(['x-www-browser', link])

        for link in self._selected:
            subprocess.call(['x-www-browser', link])

    def run(self):
        urwid.MainLoop(urwid.PopUpTarget(self), palette=PALETTE, unhandled_input=exit_program, pop_ups=True).run()
