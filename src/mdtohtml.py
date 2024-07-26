from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode
from mdtoblocks import md_to_blocks
from blocktoblocktype import block_to_block_type
from texttonode import text_to_node

def text_to_child(doc):
    child_list = []
    for child in text_to_node(doc):
        child_list.append(child.to_html_node())

    return child_list

def md_to_html(document):
    html_node = []

    for block in md_to_blocks(document):
        type = block_to_block_type(block)

        match type:
            case "heading":
                html_node.append(ParentNode(text_to_child(block.lstrip('#').lstrip(" ")),f"h{len(block.split(' ')[0])}"))
            case "code":
                html_node.append(ParentNode([
                    ParentNode(text_to_child(block.lstrip("```\n").rstrip("```")), "code")
                ], "pre"))
                
            case "quote":
                for quote in block.split("\n"):
                    html_node.append(ParentNode(text_to_child(quote.lstrip("> ")), "blockquote"))
            case "ordered_list":
                li_list = []
                for li in block.split("\n"):
                    li_list.append(ParentNode(text_to_child(li[3:]), "li"))
                html_node.append(ParentNode(li_list, "ol"))
            case "unordered_list":
                li_list = []
                for li in block.split("\n"):
                    li_list.append(ParentNode(text_to_child(li[2:]), "li"))
                html_node.append(ParentNode(li_list, "ul"))
            case "paragraph":
                html_node.append(ParentNode(text_to_child(block), "p"))
            case _:
                raise ValueError("Incorrect type")

    return ParentNode(html_node, "div", None)