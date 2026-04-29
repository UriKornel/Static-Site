# from textnode import TextNode, TextType
# from htmlnode import HTMLNode
# from test_split_nodes_delimeter import split_nodes_delimiter
from cpy import cpy
from generate_pages_recursive import generate_pages_recursive


def main():
    src = "static/"
    dest = "public/"
    cpy(src, dest)

    from_path = "content"
    template_path = "template.html"
    dest_path = "public"
    generate_pages_recursive(from_path, template_path, dest_path)

main()
