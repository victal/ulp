#coding=utf-8
import os
import shlex
import subprocess

import sys
from urwid import Frame, Divider, Text, Edit, SimpleListWalker, ListBox, ExitMainLoop, AttrWrap

COMMAND_TEMPLATE = """
# Expand aliases even when not i =n interactive mode
if type shopt > /dev/null; then
  shopt -s expand_aliases
fi
echo "Running: %s"
%s
exit;
"""


class CommandLine(Frame):

    def __init__(self, selected_links, on_exit):
        self.COMMAND_FILE = os.path.join(os.getenv('HOME'), '.cache', 'ulp', 'ulp.sh')
        self._links = selected_links
        self._on_escape = on_exit
        self._edit_field = AttrWrap(Edit(edit_text=""), "editbx", "focused")
        Frame.__init__(self, self.create_body())

    def create_body(self):
        div = Divider(div_char="=")
        return ListBox(SimpleListWalker([
            div,
            Text("Selected Links:"),
            div] +
            [Text(link) for link in self._links] +
            [
            div,
            Text("Type a command below! URLs will be appended or replace $F;"),
            Text("Press ESC to go back to the previous screen"),
            self._edit_field
        ]))

    def keypress(self, size, key):
        if key == 'enter':
            self.create_command_script()
            raise ExitMainLoop()
        elif key == 'esc':
            self._on_escape()
        else:
            return Frame.keypress(self, size, key)

        return None

    def create_command_script(self):
        command = self._edit_field.edit_text
        links = ' '.join(["'" + link + "'" for link in self._links])
        if "$F" in command:
            command = command.replace("$F", links)
        else:
            command = command + " " + links

        with open(self.COMMAND_FILE, 'w') as f:
            f.write(COMMAND_TEMPLATE % (command, command))
