import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    
    def test_default_values(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_tag(self):
        node = HTMLNode(tag="x")
        self.assertEqual(node.tag, "x")

    def test_value(self):
        node = HTMLNode(value="x")
        self.assertEqual(node.value, "x")

    def test_children(self):
        node = HTMLNode(children=[])
        self.assertEqual(node.children, [])
    
    def test_props(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props, {})

    def test_props_to_html(self):
        node = HTMLNode(props={"href":"x", "target":"y"})
        s = node.props_to_html()
        self.assertEqual(s, ' href="x" target="y"')

if __name__ == "__main__":
    unittest.main()
