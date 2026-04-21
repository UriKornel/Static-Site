import unittest
from split_nodes import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class test_split_image_link_nodes(unittest.TestCase):
    def test_split_image_nodes(self):
        nodes = TextNode("This is an image node ![image](fancy url)", TextType.TEXT)
        matches = [
            TextNode("This is an image node ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "fancy url"),
        ]
        self.assertEqual(split_nodes_image([nodes]), matches)

    def test_multiple_split_image_nodes(self):
        nodes = TextNode("This is an image ![image1](fancy url1) and another ![image2](fancy url2)", TextType.TEXT)
        matches = [
            TextNode("This is an image ", TextType.TEXT),
            TextNode("image1", TextType.IMAGE, "fancy url1"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("image2", TextType.IMAGE, "fancy url2")
        ]
        self.assertEqual(split_nodes_image([nodes]), matches)

    def test_multiple_nodes_split_image_nodes(self):
        nodes = [
            TextNode("This is an image ![image](fancy url)", TextType.TEXT),
            TextNode("This is the second ![image](fancy url2)", TextType.TEXT)
        ]
        matches = [
            TextNode("This is an image ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "fancy url"),
            TextNode("This is the second ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "fancy url2")
        ]
        self.assertEqual(split_nodes_image(nodes), matches)

    def test_split_link_nodes(self):
        nodes = TextNode("This is link node [link](fancy url)", TextType.TEXT)
        matches = [
            TextNode("This is link node ", TextType.TEXT),
            TextNode("link", TextType.LINK, "fancy url"),
        ]
        self.assertEqual(split_nodes_link([nodes]), matches)

    def test_multiple_split_link_nodes(self):
        nodes = TextNode("This is a link [link1](fancy url1) and another [link](fancy url2)", TextType.TEXT)
        matches = [
            TextNode("This is a link ", TextType.TEXT),
            TextNode("link1", TextType.LINK, "fancy url1"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("link", TextType.LINK, "fancy url2")
        ]
        self.assertEqual(split_nodes_link([nodes]), matches)


    def test_multiple_nodes_split_link_nodes(self):
        nodes = [
            TextNode("This is an link [link](fancy url)", TextType.TEXT),
            TextNode("This is the second [link2](fancy url2)", TextType.TEXT)
        ]
        matches = [
            TextNode("This is an link ", TextType.TEXT),
            TextNode("link", TextType.LINK, "fancy url"),
            TextNode("This is the second ", TextType.TEXT),
            TextNode("link2", TextType.LINK, "fancy url2")
        ]
        self.assertEqual(split_nodes_link(nodes), matches)
