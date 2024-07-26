from leafnode import LeafNode

class TextNode:
    def __init__(self, text, text_style=None, url=None):
        self.text = text
        self.text_style = text_style
        self.url = url
    
    def __eq__(self, other):
        return self.text == other.text and self.text_style == other.text_style and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_style}, {self.url})"
    
    def to_html_node(self):
        if self.text_style == "text":
            return LeafNode(self.text, None, None)
        elif self.text_style == "code":
            return LeafNode(self.text, "code", None)
        elif self.text_style == "bold":
            return LeafNode(self.text, "b", None)
        elif self.text_style == "italic":
            return LeafNode(self.text, "i", None)
        elif self.text_style == "link":
            return LeafNode(self.text, "a", {"href": self.url})
        elif self.text_style == "image":
            return LeafNode("", "img", {"alt": self.text, "src": self.url})
        else:
            raise ValueError(f"Unknown text style: {self.text_style}")
        