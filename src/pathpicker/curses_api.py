# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
import curses
import sys


class CursesAPI:

    """A dummy curses wrapper that allows us to intercept these
    calls when in a test environment"""

    def __init__(self):
        pass

    def use_default_colors(self):
        curses.use_default_colors()

    def echo(self):
        curses.echo()

    def noecho(self):
        curses.noecho()

    def init_pair(self, pair_number, fg_color, bg_color):
        return curses.init_pair(pair_number, fg_color, bg_color)

    def color_pair(self, color_number):
        return curses.color_pair(color_number)

    def get_color_pairs(self):
        assert hasattr(curses, "COLOR_PAIRS"), "curses is not initialized!"
        return curses.COLOR_PAIRS

    def exit(self):
        sys.exit(0)

    def allow_file_output(self):
        return True
