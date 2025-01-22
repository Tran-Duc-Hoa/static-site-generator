import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_extract_markdown_images_single(self):
        text = "![alt text](https://www.example.com/image.png)"
        result = extract_markdown_images(text)
        self.assertListEqual(
            [("alt text", "https://www.example.com/image.png")],
            result,
        )

    def test_extract_markdown_images_multiple(self):
        text = "![alt text](https://www.example.com/image.png) and ![another image](https://www.example.com/another.png)"
        result = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("alt text", "https://www.example.com/image.png"),
                ("another image", "https://www.example.com/another.png"),
            ],
            result,
        )

    def test_extract_markdown_images_no_images(self):
        text = "This is a text without images."
        result = extract_markdown_images(text)
        self.assertListEqual([], result)

    def test_extract_markdown_links_single(self):
        text = "[Google](https://www.google.com)"
        result = extract_markdown_links(text)
        self.assertListEqual(
            [("Google", "https://www.google.com")],
            result,
        )

    def test_extract_markdown_links_multiple(self):
        text = "[Google](https://www.google.com) and [Example](https://www.example.com)"
        result = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("Google", "https://www.google.com"),
                ("Example", "https://www.example.com"),
            ],
            result,
        )

    def test_extract_markdown_links_no_links(self):
        text = "This is a text without links."
        result = extract_markdown_links(text)
        self.assertListEqual([], result)

    def test_split_nodes_image_single(self):
        node = TextNode("This is an image ![alt text](https://www.example.com/image.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is an image ", TextType.TEXT),
                TextNode("alt text", TextType.IMAGE, "https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_nodes_image_multiple(self):
        node = TextNode("This is an image ![alt text](https://www.example.com/image.png) and another ![another image](https://www.example.com/another.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is an image ", TextType.TEXT),
                TextNode("alt text", TextType.IMAGE, "https://www.example.com/image.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("another image", TextType.IMAGE, "https://www.example.com/another.png"),
            ],
            new_nodes,
        )

    def test_split_nodes_image_no_images(self):
        node = TextNode("This is a text without images.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a text without images.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_link_single(self):
        node = TextNode("This is a link [Google](https://www.google.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a link ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com"),
            ],
            new_nodes,
        )

    def test_split_nodes_link_multiple(self):
        node = TextNode("This is a link [Google](https://www.google.com) and [Example](https://www.example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a link ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("Example", TextType.LINK, "https://www.example.com"),
            ],
            new_nodes,
        )

    def test_split_nodes_link_no_links(self):
        node = TextNode("This is a text without links.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text without links.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_text_to_textnodes_bold(self):
        text = "This is **bold** text"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
            result,
        )

    def test_text_to_textnodes_italic(self):
        text = "This is *italic* text"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
            result,
        )

    def test_text_to_textnodes_code(self):
        text = "This is `code` text"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text", TextType.TEXT),
            ],
            result,
        )

    def test_text_to_textnodes_image(self):
        text = "This is an image ![alt text](https://www.example.com/image.png)"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is an image ", TextType.TEXT),
                TextNode("alt text", TextType.IMAGE, "https://www.example.com/image.png"),
            ],
            result,
        )

    def test_text_to_textnodes_link(self):
        text = "This is a link [Google](https://www.google.com)"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is a link ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com"),
            ],
            result,
        )

    def test_text_to_textnodes_combined(self):
        text = "This is **bold**, *italic*, `code`, an image ![alt text](https://www.example.com/image.png), and a link [Google](https://www.google.com)"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(", ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(", ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(", an image ", TextType.TEXT),
                TextNode("alt text", TextType.IMAGE, "https://www.example.com/image.png"),
                TextNode(", and a link ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com"),
            ],
            result,
        )

if __name__ == "__main__":
    unittest.main()
