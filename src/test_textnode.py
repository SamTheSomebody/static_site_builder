import unittest

from text_node import TextNode, TextType, text_node_to_html_node
from html_node import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.text, "This is a text node")
 
    def test_eq_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node.url, "https://www.boot.dev")

    def test_eq_text_type_normal(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(node.text_type, TextType.NORMAL.value)

    def test_eq_text_type_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node.text_type, TextType.ITALIC.value)

    def test_eq_text_type_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.text_type, TextType.BOLD.value)

    def test_eq_text_type_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node.text_type, TextType.CODE.value)

    def test_eq_text_type_link(self):
        node = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node.text_type, TextType.LINK.value)

    def test_eq_text_type_image(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        self.assertEqual(node.text_type, TextType.IMAGE.value)

class TextTextNodeToHTMLNode(unittest.TestCase):
    def test_normal_text_node_to_html_node(self):
        text_node = TextNode("test", TextType.NORMAL)
        node = text_node_to_html_node(text_node)
        self.assertEqual(repr(node), "LeafNode(None, test, None)")

    def test_bold_text_node_to_html_node(self):
        text_node = TextNode("test", TextType.BOLD)
        node = text_node_to_html_node(text_node)
        self.assertEqual(repr(node), "LeafNode(b, test, None)")

    def test_italic_text_node_to_html_node(self):
        text_node = TextNode("test", TextType.ITALIC)
        node = text_node_to_html_node(text_node)
        self.assertEqual(repr(node), "LeafNode(i, test, None)")

    def test_code_text_node_to_html_node(self):
        text_node = TextNode("test", TextType.CODE)
        node = text_node_to_html_node(text_node)
        self.assertEqual(repr(node), "LeafNode(code, test, None)")

    def test_link_text_node_to_html_node(self):
        text_node = TextNode("test", TextType.LINK, "url")
        node = text_node_to_html_node(text_node)
        self.assertEqual(repr(node), "LeafNode(a, test, {'href': 'url'})")

    def test_image_text_node_to_html_node(self):
        text_node = TextNode("test", TextType.IMAGE, "url")
        node = text_node_to_html_node(text_node)
        self.assertEqual(repr(node), "LeafNode(img, , {'src': 'url', 'alt': 'test'})")

if __name__ == "__main__":
    unittest.main()
