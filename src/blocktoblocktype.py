import re

def block_to_block_type(block):
    if re.match(r"#{1,6} .*", block):
        return "heading"
    elif re.match(r"```\n((.*)\n*)*```\n{0,1}", block):
        return "code"
    elif re.match(r"(\> .*)", block):
        return "quote"
    elif re.match(r"(-|\*) .*", block):
        return "unordered_list"
    elif re.match(r"\d. .*", block):
        return "ordered_list"
    else:
        return "paragraph"