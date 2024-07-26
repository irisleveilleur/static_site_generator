class HTMLNode:
    def __init__(self, tag=None, value=None, attributes=None, children=None):
        self.tag = tag
        self.value = value
        self.attributes = attributes
        self.children = children

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.attributes == other.attributes and self.children == other.children
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.attributes}, {self.children})"
    
    def attributes_to_html(self):
        html = ""
        if self.attributes != None:
            for key, value in self.attributes.items():
                html += f' {key}="{value}"'
        return html
    
    def to_html(self):
        raise NotImplementedError("Implemented by subclasses")

