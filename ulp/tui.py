#!/usr/bin/env python
# coding=utf-8
import sys
import subprocess

from ulp.main import Interface
from ulp.urlextract import read_inputfile
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument('-o', '--open', dest='open', action='store_true', help='Automatically opens the URL in a browser when only one URL is found')
    args = parser.parse_args()
    choices = read_inputfile()
    if len(choices) == 0:
        print("-" * 44, file=sys.stderr)
        print("No links found in provided input, exiting...")
        sys.exit(1)
    if len(choices) == 1 and args.open:
        subprocess.call(['x-www-browser', choices[0]])
    else:
        Interface(choices).run()


if __name__ == '__main__':
    main()
