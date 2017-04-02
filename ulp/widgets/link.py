# coding=utf-8
import subprocess

from urwid import Text

SELECTED_PADDING = '|===> '


def open_item(choice):
    subprocess.call(['x-www-browser', choice])


def do_nothing(text):
    pass


class Link(Text):
    def __init__(self, link, on_select=do_nothing, align='left', wrap='space'):
        Text.__init__(self, ('unselected', link), align=align, wrap=wrap)
        self.raw_link = link
        self.selected = False
        self.on_select = on_select

    def selectable(self):
        return True

    def keypress(self, size, key):
        if key == ' ':
            self._toggle_selection()
            return None
        elif key == 'enter':
            open_item(self.raw_link)

        return key

    def _toggle_selection(self):
        self.selected = not self.selected
        self.on_select(self.raw_link)
        if self.selected:
            self.set_text(('selected', SELECTED_PADDING + self.raw_link))
        else:
            self.set_text(('unselected', self.raw_link))



