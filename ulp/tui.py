#!/usr/bi/env python
# coding=utf-8
from ulp.main import Interface
from ulp.urlextract import read_inputfile


def main():
    choices = read_inputfile()
    Interface(choices).run()


if __name__ == '__main__':
    main()