from mdtohtml import md_to_html
from htmlnode import HTMLNode
import unittest

class TestTextToNode(unittest.TestCase):
    def test_md_to_html(self):
        result = md_to_html("# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n\n```\nthis is a code snippet\n```\n\n> this is a quote\n> fwefwe\n\n1. fwefw\n2. this is an ordered list")
        self.assertEqual(result, HTMLNode(
            "div",
            None,
            None,
            [
                HTMLNode("h1", "This is a heading", None, None),
                HTMLNode("p", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.")
            ]
        ))

if __name__ == "__main__":
    unittest.main()