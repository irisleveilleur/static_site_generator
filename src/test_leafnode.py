from leafnode import LeafNode

import unittest

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("value text", "div", {"class": "bold"})
        self.assertEqual(node.to_html(), '<div class="bold">value text</div>')