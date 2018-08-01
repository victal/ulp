from ulp.urlextract import escape_ansi, parse_input
import os

TEST_DIR = os.path.dirname(os.path.realpath(__file__))

def test_parse_no_url_input():
    assert len(parse_input("")) == 0
    multiline_text = """
    text
    without URLs
    and 
    multiple lines """
    assert len(parse_input(multiline_text)) == 0

def test_extract_one_url():
    with open(os.path.join(TEST_DIR, 'example_bitbucket.txt')) as f:
        result = parse_input(f.read())
        assert len(result) == 1
        assert result[0] == 'https://bitbucket.org/owner/repository/pull-requests/new?source=BRANCH&t=1'

def test_extract_multiple_urls_per_line():
    input_text = """
    two urls
    https://example.org/?q=1 https://example.org/?p=2
    on the same line"""
    result = parse_input(input_text)
    assert len(result) == 2
    assert 'https://example.org/?q=1' in result
    assert 'https://example.org/?p=2' in result

def test_escape_ansi_sequence_url():
    with open(os.path.join(TEST_DIR, 'example_terminal_colors.txt')) as f:
        result = parse_input(f.read())
        assert len(result) == 2
        assert 'https://example.org/?p=3707' in result
        assert 'https://example.org/anotherurl?q=0m' in result
