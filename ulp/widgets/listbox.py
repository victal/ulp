from urwid import ListBox


class WrappingListBox(ListBox):

    def __init__(self, body):
        ListBox.__init__(self, body)

    def keypress(self, size, key):
        last_position = len(self.body) - 1
        if self.focus_position == 0 and key in ['up', 'page up']:
            self.change_focus(size, last_position, coming_from='below')
            return None

        if self.focus_position == last_position and key in ['down', 'page down']:
            self.change_focus(size, 0, coming_from='above')
            return None

        return ListBox.keypress(self, size, key)