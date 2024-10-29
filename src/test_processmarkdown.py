import unittest

from processmarkdown import *
from textnode import TextNode, TextType

class TestProcessMarkdown(unittest.TestCase):
    def test_bold_text(self):
        markdown = "This is a *test* string."
        node = TextNode(markdown, TextType.NORMAL)
        nodes = [node]
        result = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        self.assertEqual(len(result), 3)

    def test_italic_text(self):
        markdown = "This is a **test** string."
        node = TextNode(markdown, TextType.NORMAL)
        nodes = [node]
        result = split_nodes_delimiter(nodes, "**", TextType.ITALIC)
        self.assertEqual(len(result), 3)

    def test_code_text(self):
        markdown = "This is a `test` string."
        node = TextNode(markdown, TextType.NORMAL)
        nodes = [node]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(len(result), 3)

    def test_multiple_bold(self):
        markdown = "This *is a *test* string*."
        node = TextNode(markdown, TextType.NORMAL)
        nodes = [node]
        result = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        self.assertEqual(len(result), 5)

#    def test_nested_text(self):
#        markdown = "This **is a *test* string.**"
#        node = TextNode(markdown, TextType.NORMAL)
#        nodes = [node]
#        result = split_nodes_delimiter(nodes, "*", TextType.BOLD)
#        result = split_nodes_delimiter(result, "**", TextType.ITALIC)
#        self.assertEqual(len(result), 5)

if __name__ == "__main__":
    unittest.main()
