from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode tag cannot be None")
        if not self.children:
            raise ValueError("ParentNode children cannot be None")
        return f"<{self.tag}{self.props_to_html()}>{self.children.to_html()}</{self.tag}>"