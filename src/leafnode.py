from enum import Enum

from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode value cannot be None")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.props == other.props
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props_to_html()})"