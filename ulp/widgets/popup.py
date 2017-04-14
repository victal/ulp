#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urwid

class PopUpDialog(urwid.WidgetWrap):
    """A dialog that appears with nothing but a close button """
    signals = ['close']
    def __init__(self, inner_widget):
        close_button = urwid.Button("OK")
        urwid.connect_signal(close_button, 'click',
            lambda button:self._emit("close"))
        pile = urwid.Pile([inner_widget, close_button])
        fill = urwid.Filler(pile)
        self.__super.__init__(urwid.AttrWrap(fill, 'popup'))


class PopUpWrapper(urwid.PopUpLauncher):
    def __init__(self, original):
        self.__super.__init__(original)

    def create_popup(self, content):
        self._pop_up = PopUpDialog(content)
        urwid.connect_signal(self._pop_up, 'close',
            lambda button: self.close_pop_up())
        self.open_pop_up()

    def create_pop_up(self):
        return self._pop_up

    def get_pop_up_parameters(self):
        return {'left':10, 'top':10, 'overlay_width':80, 'overlay_height':7}

