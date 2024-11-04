import unittest
from html_node import HTMLNode, LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    
    def test_default_values(self):
        node = ParentNode("x", [])
        self.assertEqual(node.tag, "x")
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, None)

    def test_tag(self):
        node = ParentNode("x", [])
        self.assertEqual(node.tag, "x")

    def test_children(self):
        node = ParentNode(children=[], tag="y")
        self.assertEqual(node.children, [])

    def test_props(self):
        node = ParentNode(children=[], tag="y", props={})
        self.assertEqual(node.props, {})

    def test_props_to_html(self):
        node = ParentNode(children=[], tag="y", props={"href":"x", "target":"y"})
        s = node.props_to_html()
        self.assertEqual(s, ' href="x" target="y"')

    def test_to_html(self):
        childNode = LeafNode("x", "y")
        node = ParentNode("tag", [childNode])
        s = node.to_html()
        self.assertEqual(s, "<tag><x>y</x></tag>")

    def test_to_html_multiple_layers(self):
        childNode = LeafNode("x", "y")
        parentNode = ParentNode("b", [childNode])
        node = ParentNode("a", [parentNode])
        s = node.to_html()
        self.assertEqual(s, "<a><b><x>y</x></b></a>")

    def test_to_html_many_children(self):
        node = ParentNode("h2", [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>")
if __name__ == "__main__":
    unittest.main()
