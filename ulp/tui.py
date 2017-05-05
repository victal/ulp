#!/usr/bin/env python
# coding=utf-8
import sys

from ulp.main import Interface
from ulp.urlextract import read_inputfile


def main():
    choices = read_inputfile()
    if len(choices) == 0:
        print("-" * 44, file=sys.stderr)
        print("No links found in provided input, exiting...")
        sys.exit(1)

    Interface(choices).run()


if __name__ == '__main__':
    main()