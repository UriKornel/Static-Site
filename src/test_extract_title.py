import unittest
from extract_title import extract_title

class test_extract_title(unittest.TestCase):
    def test_correct_title(self):
        title_line = "# apple"
        self.assertEqual("apple", extract_title(title_line))

    def test_leading_whitespace_title(self):
        title_line = " # apple"
        self.assertEqual("apple", extract_title(title_line))

    def test_multiple_line_markdown(self):
        markdown = """
this si not a title
# title
this is also not a title

and this is also not and should not be returned
        """
        self.assertEqual("title", extract_title(markdown))

