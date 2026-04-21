import unittest
from split_nodes import split_nodes_delimiter
from textnode import TextType, TextNode

class test_split_nodes_delimeter(unittest.TestCase):
    def test_no_text_block(self):
        node = TextNode("This is a code block", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual([node], new_nodes)

    def test_text_code_text(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, answer)

    def test_text_bold_text(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, answer)

    def test_text_code(self):
        node = TextNode("This is text with a `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode("", TextType.TEXT)
            ]
        self.assertEqual(new_nodes, answer)

    def test_multiple_blocks(self):
        node = TextNode("This is text with a `code block` word and another `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word and another ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode("", TextType.TEXT)
            ]
        self.assertEqual(new_nodes, answer)

    def test_multiple_blocks_following_eachother(self):
        node = TextNode("This is text with a `two code blocks` `following code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("two code blocks", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("following code block", TextType.CODE),
            TextNode("", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, answer)

    def test_multiple_input_node(self):
        nodes = [
            TextNode("This is a node `code`", TextType.TEXT),
            TextNode("This is the second node `code`", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        answer = [
            TextNode("This is a node ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode("", TextType.TEXT),
            TextNode("This is the second node ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode("", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, answer)

    def test_italic_text(self):
        nodes = split_nodes_delimiter([TextNode("This is a node with _italic_", TextType.TEXT)], "_", TextType.ITALIC)
        new_nodes = [
            TextNode("This is a node with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode("", TextType.TEXT),
        ]
        self.assertEqual(nodes, new_nodes)

