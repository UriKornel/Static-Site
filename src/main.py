# from textnode import TextNode, TextType
# from htmlnode import HTMLNode
# from test_split_nodes_delimeter import split_nodes_delimiter
from cpy import cpy


def main():
    # prop = {
    #     "href": "https://www.google.com",
    #     "target": "_blank"
    # }
    # html = HTMLNode(None, None, None, prop)
    # print(html.props_to_html())

    # nodes = [
    #     TextNode("This is a node `code`", TextType.TEXT),
    #     TextNode("This is the second node `code`", TextType.TEXT)
    # ]
    # new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    # answer = [
    #     TextNode("This is a node ", TextType.TEXT),
    #     TextNode("code", TextType.CODE),
    #     TextNode("", TextType.TEXT),
    #     TextNode("This is the second node ", TextType.TEXT),
    #     TextNode("code", TextType.CODE)
    # ]
    # print(f"input: {nodes}")
    # print(f"output: {new_nodes}")
    # print(f"answer: {answer}")

    src = "static/"
    dest = "public/"
    cpy(src, dest)

main()
