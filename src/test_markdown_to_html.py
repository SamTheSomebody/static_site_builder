import unittest

from markdown_to_html import *

class TestMarkdownToHTML(unittest.TestCase):
    def test_has_root_div(self):
        markdown = "Test"
        result = markdown_to_html_node(markdown)
        expected = ParentNode("div", [ParentNode("p", [LeafNode(None, "Test")])])
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.props, expected.props)
        self.assertEqual(result.children[0].tag, expected.children[0].tag)
        self.assertEqual(result.children[0].props, expected.children[0].props)
        self.assertEqual(result.children[0].children[0].tag, expected.children[0].children[0].tag)
        self.assertEqual(result.children[0].children[0].value, expected.children[0].children[0].value)

    def test_heading_one_block(self):
        markdown = "# Title"
        result = markdown_to_html_node(markdown)
        expected = ParentNode("div", [ParentNode("h1", [LeafNode(None, "Title")])]) 
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.props, expected.props)
        self.assertEqual(result.children[0].tag, expected.children[0].tag)
        self.assertEqual(result.children[0].props, expected.children[0].props)

    def test_heading_six_block(self):
        markdown = "###### Title"
        result = markdown_to_html_node(markdown)
        expected = ParentNode("div", [ParentNode("h6", [LeafNode(None, "Title")])]) 
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.props, expected.props)
        self.assertEqual(result.children[0].tag, expected.children[0].tag)
        self.assertEqual(result.children[0].props, expected.children[0].props)

    def test_heading_seven_block(self):
        markdown = "####### Title"
        result = markdown_to_html_node(markdown)
        expected = ParentNode("div", [ParentNode("p", [LeafNode(None, "####### Title")])]) 
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.props, expected.props)
        self.assertEqual(result.children[0].tag, expected.children[0].tag)
        self.assertEqual(result.children[0].props, expected.children[0].props)

    def test_ordered_list_block(self):
        return None
        markdown = "1. An Ordered List Entry\n2. Another Ordered List Entry\n 3. A Final Ordered List Entry"
        result = markdown_to_html_node(markdown)
        expected = ParentNode("div", ParentNode())
        self.assertequal(result, expected)

    def test_unordered_list_block(self):
        return None
        markdown = "- An Unordered List Entry\n- Another Unordered List Entry\n- A Final Unordered List Entry"
        result = markdown_to_html_node(markdown)
        expected = ParentNode("div", ParentNode())
        self.assertequal(result, expected)

    def test_convert(self):
        return None
        markdown = "# Title\n\n## Subtitle\n\nThis is just some text\n\n1. An Ordered **List** Entry\n2. Another Ordered *List* Entry\n 3. A Final Ordered `List` Entry\n\n> I hope this works.\n\nUnordered List\n\n- Another Type of unordered list"
        result = markdown_to_html_node(markdown)
        #print(result)
        self.assertEqual(False, True)

    def test_covert_code(self):
        return None
        markdown = "# Title\n\n```\nThis is some code\n```\n"
        result = markdown_to_html_node(markdown)
        expected = ParentNode("div", [LeafNode("h1", "Title"), LeafNode("code", "This is some code")])
        #print(result)
        self.assertEqual(result, expected)
