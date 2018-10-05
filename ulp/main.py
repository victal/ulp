#!/usr/bin/env python
# coding=utf-8
import os
import subprocess

import pyperclip
import urwid

from ulp.widgets.command_line import CommandLine
from ulp.widgets.link import ClickableLink
from ulp.widgets.listbox import WrappingListBox
from ulp.widgets.popup import PopUpWrapper


def exit_program(key):
    raise urwid.ExitMainLoop()


PALETTE = [
    ('focus_selected', 'white', 'dark red'),
    ('focused', 'light gray', 'dark blue'),
    ('selected', 'white', 'light green'),
    ('unselected', 'black', ''),
    ('popup', 'light gray', 'black'),
    ('editbx', 'light gray', 'dark blue'),
    ('editcp', 'black', 'light gray', 'standout'),

]

COMMANDS = [
    ('c', 'Copy to clipboard'),
    ('Enter', 'Open in browser'),
    ('x', 'Command mode'),
    ('Space', 'Select'),
    ('q', 'Exit')
]


class Interface(urwid.Frame):

    def __init__(self, choices):
        super(Interface, self).__init__(self._create_body(choices), footer=Interface._get_help_text())
        self._selected = []
        self._main_body = self.get_body()
        self._total_choices = len(choices)

    def keypress(self, size, key):
        handled = urwid.Frame.keypress(self, size, key)
        if handled is not None:
            if key == 'c':
                self._copy_selected_to_clipboard()
            elif key == 'enter':
                self._open_links()
                exit_program(key)
            elif key == 'x':
                self.set_body(CommandLine(self.get_links(), on_exit=self.reset_body))
            elif key == 'q':
                exit_program(key)
            else:
                return key

        return None

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
            pyperclip.copy(os.linesep.join(self.get_links()))
        except pyperclip.PyperclipException as e:
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
        for link in self.get_links():
            subprocess.call(['x-www-browser', link])

    def get_links(self):
        if self._selected:
            return self._selected

        # else return current focused link
        attrmap = self.focus.original_widget.focus
        return [attrmap.original_widget.get_link()]

    def reset_body(self):
        self.set_body(self._main_body)

    def run(self):
        urwid.MainLoop(urwid.PopUpTarget(self), palette=PALETTE, unhandled_input=exit_program, pop_ups=True).run()
