import unittest
from block import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):

    # HEADING TESTS
    def test_h1(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)

    def test_h3(self):
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)

    def test_h6(self):
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_heading_no_space(self):
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.PARAGRAPH)

    def test_seven_hashes(self):
        self.assertEqual(block_to_block_type("####### Too many"), BlockType.PARAGRAPH)

    # CODE TESTS
    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\nsome code\n```"), BlockType.CODE)

    def test_code_no_newline(self):
        self.assertEqual(block_to_block_type("```some code```"), BlockType.PARAGRAPH)

    # QUOTE TESTS
    def test_single_line_quote(self):
        self.assertEqual(block_to_block_type(">some quote"), BlockType.QUOTE)

    def test_multiline_quote(self):
        self.assertEqual(block_to_block_type(">line one\n>line two\n>line three"), BlockType.QUOTE)

    def test_quote_with_space(self):
        self.assertEqual(block_to_block_type("> quote with space"), BlockType.QUOTE)

    def test_quote_missing_marker(self):
        self.assertEqual(block_to_block_type(">line one\nline two"), BlockType.PARAGRAPH)

    # UNORDERED LIST TESTS
    def test_single_item_unordered(self):
        self.assertEqual(block_to_block_type("- item one"), BlockType.UNORDERED_LIST)

    def test_multiline_unordered(self):
        self.assertEqual(block_to_block_type("- item one\n- item two\n- item three"), BlockType.UNORDERED_LIST)

    def test_unordered_missing_marker(self):
        self.assertEqual(block_to_block_type("- item one\nitem two"), BlockType.PARAGRAPH)

    # ORDERED LIST TESTS
    def test_single_item_ordered(self):
        self.assertEqual(block_to_block_type("1. item one"), BlockType.ORDERED_LIST)

    def test_multiline_ordered(self):
        self.assertEqual(block_to_block_type("1. item one\n2. item two\n3. item three"), BlockType.ORDERED_LIST)

    def test_ordered_wrong_start(self):
        self.assertEqual(block_to_block_type("2. starts at two"), BlockType.PARAGRAPH)

    def test_ordered_skips_number(self):
        self.assertEqual(block_to_block_type("1. item one\n3. skips two"), BlockType.PARAGRAPH)

    # PARAGRAPH TESTS
    def test_plain_paragraph(self):
        self.assertEqual(block_to_block_type("just some text"), BlockType.PARAGRAPH)

    def test_multiline_paragraph(self):
        self.assertEqual(block_to_block_type("line one\nline two"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()