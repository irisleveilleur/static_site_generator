from splitnodes import split_nodes, split_image_nodes, split_link_nodes
from textnode import TextNode
import unittest

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes(self):
        result = split_nodes([TextNode("This is text with a **bolded phrase** in the middle", "text", None)], "**", "bold")
        self.assertEqual(result, [
            TextNode("This is text with a ", "text"),
            TextNode("bolded phrase", "bold"),
            TextNode(" in the middle", "text"),
        ])
    
    def test_split_image_nodes(self):
        result = split_image_nodes([TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", "text", None)])
        self.assertEqual(result, [
            TextNode("This is text with a ", "text"),
            TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", "text"),
            TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg")
        ])
    
    def test_split_link_nodes(self):
        result = split_link_nodes([TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", "text", None)])
        self.assertEqual(result, [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev")
        ])

if __name__ == "__main__":
    unittest.main()