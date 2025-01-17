from leafnode import LeafNode
from textnode import TextType

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode(text_node.text, "b")
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(text_node.text, "i")
    if text_node.text_type == TextType.CODE:
        return LeafNode(text_node.text, "code")
    if text_node.text_type == TextType.LINK:
        return LeafNode(text_node.text, "a", {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Unknown TextType: {text_node.text_type}")