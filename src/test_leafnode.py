import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode('p', 'This is a text node', { 'style': 'color: red' })
        node2 = LeafNode('p', 'This is a text node', { 'style': 'color: red' })
        self.assertEqual(node, node2)

    def test_neq(self):
        node = LeafNode('p', 'This is a text node')
        node2 = LeafNode('a', 'This is a text node')
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = LeafNode('p', 'This is a text node', { 'style': 'color: red' }).props_to_html()
        node2 = LeafNode('p', 'This is a text node', { 'style': 'color: red' }).props_to_html()
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()