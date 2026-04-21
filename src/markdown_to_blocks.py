def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.split("\n\n"):
        if block == "":
            continue

        block = block.strip()
        block = block.strip("\n")
        blocks.append(block)
    return blocks

