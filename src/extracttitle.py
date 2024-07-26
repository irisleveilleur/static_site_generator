from mdtoblocks import md_to_blocks
from blocktoblocktype import block_to_block_type

def extract_title(doc):
    should_be_header = md_to_blocks(doc)[0]

    if block_to_block_type(should_be_header) == "heading" and len(should_be_header.split(" ")[0]) == 1:
        return should_be_header.lstrip("# ")
    
    raise Exception("No title")
