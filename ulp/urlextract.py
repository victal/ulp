# coding=utf-8
import re
import os
import sys

# Regex for matching URLs
# See https://mathiasbynens.be/demo/url-regex
url_regex = re.compile(r"((https?|ftp)://(-\.)?([^\s/?\.#-]+\.?)+(/[^\s]*)?)")
INPUT_FILE = os.path.join(os.getenv('HOME'), '.cache', 'ulp', 'links')

def parse_stdin():
    stdin = [line.strip() for line in sys.stdin]
    print(os.linesep.join(stdin).strip(), file=sys.stderr)
    return parse_input(os.linesep.join(stdin))

def parse_input(text):
    matches = url_regex.findall(text.strip())
    return [result[0] for result in matches]

def read_inputfile():
    with open(INPUT_FILE) as f:
        return [l.strip() for l in f.readlines()]

def main():
    #If we are not being piped, exit
    if sys.stdin.isatty():
        sys.exit(1)

    result = parse_stdin()
    for url in result:
        print(url)

if __name__ == '__main__':
    main()
