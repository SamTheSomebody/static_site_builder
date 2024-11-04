import unittest

from markdown_blocks import *

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

class TestConvertToBlockTypes(unittest.TestCase):
    def test_block_to_heading_block(self):
        block = "# Test"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_block_to_heading_block_lots(self):
        block = "###### Test"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_block_to_code_block(self):
        block = "``` Test ```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_block_to_quote_block(self):
        block = "> Test\n> Case\n> Foo"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_block_to_unordered_list_star(self):
        block = "* Test\n* Case\n* Foo\n* Bar"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_block_to_unordered_list_dash(self):
        block = "- Test\n- Case\n- Foo\n- Bar"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)
     
    def test_block_to_ordered_list(self):
        block = "1. Test\n2. Case\n3. Foo\n4. Bar"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_block_to_paragraph_basic(self):
        block = "Test Case"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)
        
    def test_block_to_paragraph_not_quite_code(self):
        block = "'' Test Case ''"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)
        
    def test_block_to_paragraph_too_many_headings(self):
        block = "####### Test Case"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)
        
