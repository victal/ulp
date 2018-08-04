# coding=utf-8
import re
import os
import sys

# Regex for matching URLs
# See https://mathiasbynens.be/demo/url-regex
url_regex = re.compile(r"((https?|ftp)://(-\.)?([^\s/?\.#-]+\.?)+(/[^\s]*)?)")

ansi_escape_regex = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]", re.IGNORECASE)
INPUT_FILE = os.path.join(os.path.expanduser('~'), '.cache', 'ulp', 'links')

def escape_ansi(text):
    return ansi_escape_regex.sub("", text)

def parse_stdin():
    lines = [line.strip() for line in sys.stdin]
    print(os.linesep.join(lines).strip(), file=sys.stderr)
    return parse_input(os.linesep.join(lines))

def parse_input(text):
    matches = url_regex.findall(escape_ansi(text.strip()))
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
