import unittest

from block_text_to_text_node import *
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
    def test_extract_image_nothing(self):
        text = ""
        result = extract_markdown_images(text)
        expected = []
        self.assertListEqual(result, expected)

    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertListEqual(result, expected)
     
    def test_split_image(self):
        markdown = "This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)"
        node = TextNode(markdown, TextType.NORMAL)
        nodes = [node]
        result = split_nodes_images(nodes)
        expected =  [
            TextNode("This is text with an image ", TextType.NORMAL),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertListEqual(result, expected)


class TestExtractLink(unittest.TestCase):
    def test_extract_link_nothing(self):
        text = ""
        result = extract_markdown_links(text)
        expected = []
        self.assertListEqual(result, expected)

    def test_extract_link(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_links(text)
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertListEqual(result, expected)
   
    def test_split_link(self):
        markdown = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node = TextNode(markdown, TextType.NORMAL)
        nodes = [node]
        result = split_nodes_links(nodes)
        expected =  [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertListEqual(result, expected)

class TestExtractAll(unittest.TestCase):
    def test_all_types(self):
        markdown = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)" 
        result = text_to_textnodes(markdown)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
