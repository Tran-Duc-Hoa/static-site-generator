import unittest

from main import text_node_to_html_node
from textnode import TextNode, TextType
from leafnode import LeafNode


class TestTextNodeToHTML(unittest.TestCase):
    def test_eq(self):
        node = text_node_to_html_node(TextNode('This is a link', TextType.LINK, 'https://www.google.com'))
        node2 = LeafNode('This is a link', 'a', { 'href': 'https://www.google.com' })
        self.assertEqual(node, node2)

    def test_text_bold(self):
        node = text_node_to_html_node(TextNode('This is a bold text', TextType.BOLD))
        node2 = LeafNode('This is a bold text', 'b')
        self.assertEqual(node, node2)

    def test_text_italic(self):
        node = text_node_to_html_node(TextNode('This is an italic text', TextType.ITALIC))
        node2 = LeafNode('This is an italic text', 'i')
        self.assertEqual(node, node2)

    def test_neq(self):
        node = text_node_to_html_node(TextNode('This is a text node', TextType.BOLD))
        node2 = LeafNode('This is a text node')
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()