from mdtoblocks import md_to_blocks
import unittest

class TestTextToNode(unittest.TestCase):
    def test_md_to_blocks(self):
        result = md_to_blocks("# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item")
        self.assertEqual(result, ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"])

if __name__ == "__main__":
    unittest.main()