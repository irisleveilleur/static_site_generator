from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode
from mdtoblocks import md_to_blocks
from blocktoblocktype import block_to_block_type
from texttonode import text_to_node

def md_to_html(document):
    html_node = []

    for block in md_to_blocks(document):
        type = block_to_block_type(block)

        match type:
            case "heading":
                html_node.append(LeafNode(block.lstrip('#').lstrip(" "),f"h{len(block.split(' ')[0])}"))
            case "code":
                html_node.append(ParentNode([
                    ParentNode(text_to_node(block.strip("```")), "code")
                ], "pre"))
            case "quote":
                quote_list = []
                for quote in block.split("\n"):
                    quote_list.append(ParentNode(text_to_node(quote.lstrip("> ")), "p"))
                html_node.append(ParentNode(quote_list, "blockquote"))
            case "ordered_list":
                li_list = []
                for li in block.split("\n"):
                    li_list.append(ParentNode(text_to_node(li[3:]), "li"))
                html_node.append(ParentNode(li_list, "ol"))
            case "unordered_list":
                li_list = []
                for li in block.split("\n"):
                    li_list.append(ParentNode(text_to_node(li[2:]), "li"))
                html_node.append(ParentNode(li_list, "ul"))
            case "paragraph":
                html_node.append(ParentNode(text_to_node(block), "p"))
            case _:
                raise ValueError("Incorrect type")

    return ParentNode(html_node, "div", None)

a = md_to_html("# This is a heading\n\nThis is a\n\n```\nparagraph```\n\n of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item")
print(a)