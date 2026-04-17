import unittest
from extract_markdown_images import extract_markdown_images
from extract_markdown_links import extract_markdown_links

class text_markdown_link_extraction(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and this is another ![image](imgur.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image", "imgur.png")], matches)


    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is a text with a [link](www.boot.dev)"
        )
        self.assertListEqual([("link", "www.boot.dev")], matches)

    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links(
            "This is a text with a [link](www.boot.dev) and [link to google](google.com)"
        )
        self.assertListEqual([("link", "www.boot.dev"), ("link to google", "google.com")], matches)


