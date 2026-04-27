import unittest
from markdown_to_blocks import BlockType, block_to_block_type

class test_blocktype(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        markdown = "# heading"
        self.assertEqual(block_to_block_type(markdown),BlockType.HEADING)

    def test_block_to_block_type_heading2(self):
        markdown = "## heading"
        self.assertEqual(block_to_block_type(markdown),BlockType.HEADING)

    def test_block_to_block_type_heading3(self):
        markdown = "### heading"
        self.assertEqual(block_to_block_type(markdown),BlockType.HEADING)

    def test_block_to_block_type_heading4(self):
        markdown = "#### heading"
        self.assertEqual(block_to_block_type(markdown),BlockType.HEADING)

    def test_block_to_block_type_heading5(self):
        markdown = "##### heading"
        self.assertEqual(block_to_block_type(markdown),BlockType.HEADING)

    def test_block_to_block_type_heading6(self):
        markdown = "###### heading"
        self.assertEqual(block_to_block_type(markdown),BlockType.HEADING)

    def test_block_to_block_type_CODE(self):
        markdown = "```\ncode\n```"
        self.assertEqual(block_to_block_type(markdown),BlockType.CODE)

    def test_block_to_block_type_quote(self):
        markdown = ">quote"
        self.assertEqual(block_to_block_type(markdown),BlockType.QUOTE)

    def test_block_to_block_type_quote2(self):
        markdown = "> quote"
        self.assertEqual(block_to_block_type(markdown),BlockType.QUOTE)

    def test_block_to_block_type_unordered(self):
        markdown = "- unordered list\n- ordered list second line\n- third line"
        self.assertEqual(block_to_block_type(markdown), BlockType.ULIST)

    def test_block_to_block_type_ordered_list(self):
        markdown = "1. first line\n2. second line\n3. third line"
        self.assertEqual(block_to_block_type(markdown), BlockType.OLIST)
