from markdown_blocks import markdown_to_blocks


def extract_title(html):
    blocks = markdown_to_blocks(html)
    for block in blocks:
        if block.startswith("# "):
            return block[2:]

    raise Exception("No title found")
