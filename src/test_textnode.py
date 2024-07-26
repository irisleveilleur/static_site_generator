import unittest

from textnode import TextNode
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")
    def test_to_html_node(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.to_html_node(), LeafNode("This is a text node", "b", None))

if __name__ == "__main__":
    unittest.main()