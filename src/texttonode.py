from splitnodes import split_nodes, split_link_nodes, split_image_nodes
from textnode import TextNode

def text_to_node(text):
    nodes = [TextNode(text, "text")]
    nodes = split_nodes(nodes, "**", "bold")
    nodes = split_nodes(nodes, "*", "italic")
    nodes = split_nodes(nodes, "`", "code")
    nodes = split_image_nodes(nodes)
    nodes = split_link_nodes(nodes)
    return nodes