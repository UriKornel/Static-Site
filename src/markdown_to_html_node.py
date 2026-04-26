from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def text_to_children(string):
    text_nodes = text_to_textnodes(string)
    return [text_node_to_html_node(text) for text in text_nodes]

def lines_to_unordered_list_children(lines):
    children = []
    for line in lines:
        text_nodes = text_to_textnodes(line.split("- ", 1)[1])
        children.append([text_node_to_html_node(text) for text in text_nodes])
    return children

def lines_to_ordered_list_children(lines):
    children = []
    for line in lines:
        text_nodes = text_to_textnodes(line.split(". ", 1)[1])
        children.append([text_node_to_html_node(text) for text in text_nodes])
    return children


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            level = block.split(" ", 1)[0].count("#")
            tag = f"h{level}"
            nodes.append(ParentNode(tag, text_to_children(block.split(" ",1 )[1])))
        elif block_type == BlockType.CODE:
            code = TextNode(block[4:-3], TextType.TEXT)
            html_code = text_node_to_html_node(code)
            nodes.append(ParentNode("pre", [ParentNode("code", [html_code])]))
        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            nodes.append(ParentNode("ul", [ParentNode("li", list_item) for list_item in lines_to_unordered_list_children(lines)]))
        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            nodes.append(ParentNode("ol", [ParentNode("li", list_item) for list_item in lines_to_ordered_list_children(lines)]))
        elif block_type == BlockType.QUOTE:
            quotes = block.split("\n")
            quote_block = ""
            for quote in quotes:
                quote_block += quote.lstrip("> ")
            nodes.append(ParentNode("blockquote", text_to_children(quote_block)))
        elif block_type == BlockType.PARAGRAPH:
            nodes.append(ParentNode("p", text_to_children(block.replace("\n", " ").strip())))

    return ParentNode("div", nodes)
