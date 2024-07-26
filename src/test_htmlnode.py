import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a text node", {"class": "bold"}, None)
        node2 = HTMLNode("div", "This is a text node", {"class": "bold"}, None)
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = HTMLNode("div", "This is a text node", {"class": "bold"}, None)
        self.assertEqual(repr(node), "HTMLNode(div, This is a text node, {'class': 'bold'}, None)")
    
    def test_attributes_to_html(self):
        node = HTMLNode("div", "This is a text node", {"class": "bold", "id": "my-id"}, None)
        self.assertEqual(node.attributes_to_html(), ' class="bold" id="my-id"')


if __name__ == "__main__":
    unittest.main()