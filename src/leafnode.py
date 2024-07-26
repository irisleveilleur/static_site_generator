from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, attributes=None):
        super().__init__(tag, value, attributes, None)
    
    def to_html(self):
        if not self.value and self.tag != "img":
            raise ValueError("LeafNode value cannot be empty")
        
        if not self.tag:
            return self.value
        
        if self.tag == "img":
            return f"<{self.tag}{self.attributes_to_html()}>"
        else:
            return f"<{self.tag}{self.attributes_to_html()}>{self.value}</{self.tag}>"