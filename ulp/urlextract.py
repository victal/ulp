# coding=utf-8
import re
import sys

# Regex for matching URLs
# See https://mathiasbynens.be/demo/url-regex
url_regex = re.compile(r"((https?|ftp)://(-\.)?([^\s/?\.#-]+\.?)+(/[^\s]*)?)")


def parse_stdin():
    stdin = sys.stdin.read()
    return parse_input(stdin)


def parse_input(text):
    matches = url_regex.findall(text.strip())
    return [result[0] for result in matches]


if __name__ == '__main__':
    for link in parse_stdin():
        print(link)
