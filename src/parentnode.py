from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, children, tag, attributes=None):
        super().__init__(tag, None, attributes, children)

    def to_html(self):
        if not self.children:
            raise ValueError("ParentNode children cannot be empty")
        if not self.tag:
            raise ValueError("ParentNode tag cannot be empty")
        
        children_html = ""

        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}{self.attributes_to_html()}>{children_html}</{self.tag}>"