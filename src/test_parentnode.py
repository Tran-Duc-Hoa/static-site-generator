import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode('div', ParentNode('p', LeafNode('hi', 'span')), { 'style': 'color: red' })
        html = node.to_html()
        self.assertEqual(html, '<div style="color: red"><p><span>hi</span></p></div>')


if __name__ == "__main__":
    unittest.main()