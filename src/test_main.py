import unittest
from main import *

class TestMain(unittest.TestCase):
    def test_extract_heading(self):
        markdown = "# title"
        result = extract_title(markdown)
        expected = "title"
        self.assertEqual(result, expected)

    def test_extract_heading_with_newlines(self):
        markdown = "from\n to # title\n\nfoo\nbar"
        result = extract_title(markdown)
        expected = "title"
        self.assertEqual(result, expected)
