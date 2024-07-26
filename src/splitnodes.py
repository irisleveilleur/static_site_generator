from textnode import TextNode
from extracttags import extract_images, extract_links
import re

def split_nodes(nodes, delimiter, node_type):
    new_nodes = []

    for node in nodes:
        split_strings = node.text.split(delimiter)

        if len(split_strings) == 1:
            new_nodes.append(node)
            continue
        
        if len(split_strings) % 2 == 0:
            raise Exception("Badly marked")
        else:
            for i in range(0, len(split_strings)):
                if i % 2 == 0:
                    if split_strings[i] != "":
                        new_nodes.append(TextNode(split_strings[i], node.text_style))
                else:
                    new_nodes.append(TextNode(split_strings[i], node_type))
    return new_nodes

def split_link_nodes(nodes):
    new_nodes = []

    for node in nodes:
        if re.search("\[(.*?)\]\((.*?)\)", node.text) == None:
            new_nodes.append(node)

        extracted_links = extract_links(node.text)
        to_be_split = node.text
        for link in extracted_links:
            split_text = to_be_split.split(f"[{link[0]}]({link[1]})", 1)
            to_be_split = split_text[1]
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], "text"))
            new_nodes.append(TextNode(link[0], "link", link[1]))
            if re.search("\[(.*?)\]\((.*?)\)", split_text[1]) == None and split_text[1] != "":
                new_nodes.append(TextNode(split_text[1], "text"))

    return new_nodes

def split_image_nodes(nodes):
    new_nodes = []

    for node in nodes:
        if re.search("!\[(.*?)\]\((.*?)\)", node.text) == None:
            new_nodes.append(node)

        extracted_images = extract_images(node.text)
        to_be_split = node.text
        for image in extracted_images:
            split_text = to_be_split.split(f"![{image[0]}]({image[1]})", 1)
            to_be_split = split_text[1]
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], "text"))
            new_nodes.append(TextNode(image[0], "image", image[1]))
            if re.search("!\[(.*?)\]\((.*?)\)", split_text[1]) == None and split_text[1] != "":
                new_nodes.append(TextNode(split_text[1], "text"))

    return new_nodes