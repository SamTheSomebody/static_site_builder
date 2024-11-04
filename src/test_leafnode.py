import unittest

from html_node import LeafNode

class TestLeafNode(unittest.TestCase):
    
    def test_default_values(self):
        node = LeafNode(value="x", tag="y")
        self.assertEqual(node.tag, "y")
        self.assertEqual(node.value, "x")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_tag(self):
        node = LeafNode(value="x", tag="y")
        self.assertEqual(node.tag, "y")

    def test_value(self):
        node = LeafNode(value="x", tag="y")
        self.assertEqual(node.value, "x")

    def test_props(self):
        node = LeafNode(value="x", tag="y", props={})
        self.assertEqual(node.props, {})

    def test_to_html_without_tag(self):
        node = LeafNode(value="x", tag=None, props={"href":"x"})
        s = node.to_html()
        self.assertEqual(s, "x")
    
    def test_to_html_with_tag(self):
        node = LeafNode(value="x", tag="y", props={"href":"x"})
        s = node.to_html()
        self.assertEqual(s, '<y href="x">x</y>')

if __name__ == "__main__":
    unittest.main()
