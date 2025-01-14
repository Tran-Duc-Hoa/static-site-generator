import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('p', 'This is a text node', '<a>hi</a>', { 'style': 'color: red' })
        node2 = HTMLNode('p', 'This is a text node', '<a>hi</a>', { 'style': 'color: red' })
        self.assertEqual(node, node2)

    def test_neq(self):
        node = HTMLNode('p', 'This is a text node')
        node2 = HTMLNode('a', 'This is a text node')
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode('p', 'This is a text node', None, { 'style': 'color: red' }).props_to_html()
        node2 = HTMLNode('p', 'This is a text node', None, { 'style': 'color: red' }).props_to_html()
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()