from mdtohtml import md_to_html
from htmlnode import HTMLNode
import unittest

class TestTextToNode(unittest.TestCase):
 """    def test_md_to_html(self):
        result = md_to_html("# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n\n```\nthis is a code snippet\n```\n\n> this is a quote\n> fwefwe\n\n1. fwefw\n2. this is an ordered list")
        self.assertEqual(result, 
            HTMLNode("div", None, None, [
                HTMLNode("h1", None, None, [
                    HTMLNode("span", "This is a heading", None, None)
                ]), 
                HTMLNode("p", None, None, [
                    HTMLNode("span", "This is a paragraph of text. It has some ", None, None), 
                    HTMLNode("b", "bold", None, None), 
                    HTMLNode("span", " and ", None, None), 
                    HTMLNode("i", "italic", None, None), 
                    HTMLNode("span", " words inside of it.", None, None)
                ]), 
                HTMLNode("ul", None, None, [
                    HTMLNode("li", None, None, [
                        HTMLNode("span", "This is the first list item in a list block", None, None)
                    ]), 
                    HTMLNode("li", None, None, [
                        HTMLNode("span", "This is a list item", None, None)
                    ]), 
                    HTMLNode("li", None, None, [
                        HTMLNode("span", "This is another list item", None, None)
                    ])
                ]), 
                HTMLNode("pre", None, None, [
                    HTMLNode("code", None, None, [
                        HTMLNode("span", "this is a code snippet", None, None)
                    ])
                ]), 
                HTMLNode("blockquote", None, None, [
                    HTMLNode("p", None, None, [
                        HTMLNode("span", "this is a quote", None, None)
                    ]), 
                    HTMLNode("p", None, None, [
                        HTMLNode("span", "fwefwe", None, None)
                    ])
                ]), 
                HTMLNode("ol", None, None, [
                    HTMLNode("li", None, None, [
                        HTMLNode("span", "fwefw", None, None)
                    ]), 
                    HTMLNode("li", None, None, [
                        HTMLNode("span", "this is an ordered list", None, None)
                    ])
                ])
            ])
        ) """

if __name__ == "__main__":
    unittest.main()