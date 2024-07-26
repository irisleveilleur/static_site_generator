def md_to_blocks(document):
    document = document.strip("\n")
    return document.split("\n\n")
