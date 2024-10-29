import unittest

from processmarkdown import *
from textnode import TextNode, TextType

class TestProcessMarkdown(unittest.TestCase):
    def test_bold_text(self):
        markdown = "This is a **test** string."
        node = TextNode(markdown, TextType.NORMAL)
        nodes = [node]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This is a ", TextType.NORMAL),
            TextNode("test", TextType.BOLD),
            TextNode(" string.", TextType.NORMAL),
        ]
        self.assertListEqual(result, expected)

    def test_italic_text(self):
        markdown = "This is a *test* string."
        node = TextNode(markdown, TextType.NORMAL)
        nodes = [node]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        expected = [
            TextNode("This is a ", TextType.NORMAL),
            TextNode("test", TextType.ITALIC),
            TextNode(" string.", TextType.NORMAL),
        ]
        self.assertListEqual(result, expected)

    def test_code_text(self):
        markdown = "This is a `test` string."
        node = TextNode(markdown, TextType.NORMAL)
        nodes = [node]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [
            TextNode("This is a ", TextType.NORMAL),
            TextNode("test", TextType.CODE),
            TextNode(" string.", TextType.NORMAL),
        ]
        self.assertListEqual(result, expected)

    def test_multiple_bold(self):
        markdown = "This **is a **test** string**."
        node = TextNode(markdown, TextType.NORMAL)
        nodes = [node]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This ", TextType.NORMAL),
            TextNode("is a ", TextType.BOLD),
            TextNode("test", TextType.NORMAL),
            TextNode(" string", TextType.BOLD),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertListEqual(result, expected)

    def test_nested_text(self):
        markdown = "This `is a **test** string.`"
        node = TextNode(markdown, TextType.NORMAL)
        nodes = [node]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        result = split_nodes_delimiter(result, "**", TextType.BOLD)
        expected = [
            TextNode("This ", TextType.NORMAL),
            TextNode("is a **test** string.", TextType.CODE),
            TextNode("", TextType.NORMAL),
        ]
        self.assertListEqual(result, expected)

class TestExtractImage(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertListEqual(result, expected)
if __name__ == "__main__":
    unittest.main()
