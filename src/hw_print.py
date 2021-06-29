#!/usr/bin/env python3

# Line endings
NEXT = '\n  '
END = '\n\n'

# Term colors
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
PURPLE = '\033[35m'
RED = '\033[91m'
CYAN = '\033[36m'
END_COLOR = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# Unicode glyphs
RIGHT_ARROW = ' \u2192 '  # prints '→'

# Clears line
CLEAR = '\x1b[1A\x1b[2K'


class HomeworkPrint(object):
    """
    Provides methods for formatted output, like adding some color

    Requires: lab section, function, and optional description
    Example: HomeworkPrint('part1', function1, desc="Does something cool")
    """

    def __init__(self, func, show_args=None, desc=''):
        """
        :param part_num: Part number/section for the assignment
        :param func: Function used for a given assignment part
        :param desc: What the lab part is supposed to do
        :param show_args: Control which input arguments to print
        """
        self.desc = desc
        self.func = func
        self.show_args = show_args

    def output(self, *args, el=NEXT):
        """
        :param args: Arguments used by the function
        :param el: End line. Use NEXT for same section and END for new section 
        """
        print("%s%s" % (self.func.__name__, self.pretty_args(args)), end=RIGHT_ARROW)
        print(BOLD + GREEN + "%s" % self.func(*args) + END_COLOR, end=el)

    def heading(self, el=NEXT):
        """
        Adds an some color and an underline to clearly distinguish exercises

        :param el: End line. Use NEXT for same section and END for new section 
        """
        print(UNDERLINE + YELLOW + "%s" % (self.desc) + END_COLOR, end=el)

    def pretty_args(self, args):
        """
        :param args: list of args for the given function
        :return: 'pretty' formatted args list for console output
        """
        arg_list = []
        # If None, show all arguments. Otherwise only show the specified ones in the console
        if self.show_args is None:
            arg_list = args
        else:
            for i in self.show_args:
                arg_list.append(args[i])
        arg_str = '('
        for i in arg_list[:-1]:
            arg_str += str(i) + ", "
        arg_str += str(arg_list[-1]) + ")"
        return arg_str


def is_windows():
    """Checks if OS is Windows"""
    from os import name
    return name == 'nt'


# Use on Window's systems to enable terminal colors
def enable_ansi():
    """Allows using the ANSI codes in Windows"""
    if is_windows:
        from subprocess import call
        call('', shell=True)

