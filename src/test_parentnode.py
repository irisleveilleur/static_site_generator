from parentnode import ParentNode
from leafnode import LeafNode

import unittest

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode([LeafNode("leaf text", "p", {"class": "bold"})], "div", {"id": "my-id"})
        self.assertEqual(node.to_html(), '<div id="my-id"><p class="bold">leaf text</p></div>')
    def test_to_html_leaf_no_tag(self):
        node = ParentNode([LeafNode("leaf text"), LeafNode("leaf text"), LeafNode("leaf text")], "div", {"id": "my-id"})
        self.assertEqual(node.to_html(), '<div id="my-id">leaf textleaf textleaf text</div>')