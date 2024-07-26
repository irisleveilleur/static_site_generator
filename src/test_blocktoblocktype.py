from blocktoblocktype import block_to_block_type
from textnode import TextNode
import unittest

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        result = block_to_block_type("# fwefwefwef")
        self.assertEqual(result, "heading")
        result = block_to_block_type("## fwefwefwef")
        self.assertEqual(result, "heading")
        result = block_to_block_type("### fwefwefwef")
        self.assertEqual(result, "heading")
        result = block_to_block_type("#### fwefwefwef")
        self.assertEqual(result, "heading")
        result = block_to_block_type("##### fwefwefwef")
        self.assertEqual(result, "heading")
        result = block_to_block_type("###### fwefwefwef")
        self.assertEqual(result, "heading")
    
    def test_quote(self):
        result = block_to_block_type("> fwefwefwef\n> fwfewf")
        self.assertEqual(result, "quote")
    
    def test_paragraph(self):
        result = block_to_block_type("fwefwefwef")
        self.assertEqual(result, "paragraph")
    
    def test_code(self):
        result = block_to_block_type("```\nfwefwefwen\n```")
        self.assertEqual(result, "code")
    
    def test_ul(self):
        result = block_to_block_type("* fwefwefwef")
        self.assertEqual(result, "unordered_list")
        result = block_to_block_type("- fwefwefwef")
        self.assertEqual(result, "unordered_list")
    
    def test_ol(self):
        result = block_to_block_type("4. wweew\n 5. fwefwe")
        self.assertEqual(result, "ordered_list")
        

if __name__ == "__main__":
    unittest.main()