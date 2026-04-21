from enum import Enum

class BlockType(Enum):
    PARAGRAPH = ""
    HEADING = "#"
    CODE = "```"
    QUOTE = ">"
    UNORDERED_LIST = "_"
    ORDERED_LIST = "."

def block_to_block_type(markdown):
    if markdown[0:2] == "# ":
        return BlockType.HEADING

    if markdown[0:3] == "## ":
        return BlockType.HEADING

    if markdown[0:4] == "### ":
        return BlockType.HEADING

    if markdown[0:5] == "#### ":
        return BlockType.HEADING

    if markdown[0:6] == "##### ":
        return BlockType.HEADING

    if markdown[0:7] == "###### ":
        return BlockType.HEADING

    if markdown[0:4] == "```\n" and markdown[-3:]:
        return BlockType.CODE

    if markdown[0] == ">" or markdown[0:2] == "> ":
        return BlockType.QUOTE

    unordered_list = False
    lines = markdown.split("\n")
    for line in lines:
        if line[0:2] == "- ":
            unordered_list = True
        else:
            unordered_list = False
            break
    if unordered_list:
        return BlockType.UNORDERED_LIST


    ordered_list = False
    for i in range(len(lines)):
        line = lines[i]
        if line[0:3] == f"{i+1}. ":
            ordered_list = True
        else:
            ordered_list = False
            break
    if ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

