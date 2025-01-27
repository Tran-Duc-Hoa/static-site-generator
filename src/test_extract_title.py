import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_with_title(self):
        html = "# My Title\n\nSome content"
        self.assertEqual(extract_title(html), "My Title")

    def test_extract_title_without_title(self):
        html = "Some content without a title"
        with self.assertRaises(Exception) as context:
            extract_title(html)
        self.assertTrue("No title found" in str(context.exception))

    def test_extract_title_with_multiple_titles(self):
        html = "# First Title\n\nSome content\n\n# Second Title\n\nMore content"
        self.assertEqual(extract_title(html), "First Title")

    def test_extract_title_with_different_header_levels(self):
        html = "## Subtitle\n\n# Main Title\n\nSome content"
        self.assertEqual(extract_title(html), "Main Title")


if __name__ == '__main__':
    unittest.main()
