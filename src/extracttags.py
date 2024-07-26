import re

def extract_images(text):
    return re.findall("!\[(.*?)\]\((.*?)\)", text)

def extract_links(text):
    return re.findall("\[(.*?)\]\((.*?)\)", text)