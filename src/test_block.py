import unittest

from block import *

class TestSplitBlocks(unittest.TestCase):
    def test_split_blocks(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        result = markdown_to_blocks(markdown)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertListEqual(result, expected)

    def test_split_blocks_excess_newlines(self):
        markdown = "One\n\n\nTwo\n\n\n\nThree"
        result = markdown_to_blocks(markdown)
        expected = [
            "One",
            "Two",
            "Three",
        ]
        self.assertListEqual(result, expected)

    def test_split_blocks_excess_spacing(self):
        markdown = "A     \n\n B   "
        result = markdown_to_blocks(markdown)
        expected = [
            "A",
            "B",
        ]
        self.assertListEqual(result, expected)


