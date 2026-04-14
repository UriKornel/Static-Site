import unittest 
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        prop = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode(None, None, None, prop)
        attr =  ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), attr)

    def test_props_two(self):
        prop = {
            "href": "https://www.google.com",
            "target": "_blank",
            "foo": "bar"
        }
        node = HTMLNode(None, None, None, prop)
        attr =  ' href="https://www.google.com" target="_blank" foo="bar"'
        self.assertEqual(node.props_to_html(), attr)

    def test_props_three(self):
        prop = {
            "href": "https://www.imgur.com",
            "target": "mammamia",
            "foo": "bar"
        }
        node = HTMLNode(None, None, None, prop)
        attr =  ' href="https://www.imgur.com" target="mammamia" foo="bar"'
        self.assertEqual(node.props_to_html(), attr)

