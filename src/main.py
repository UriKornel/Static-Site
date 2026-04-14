from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    prop = {
        "href": "https://www.google.com",
        "target": "_blank"
    }
    html = HTMLNode(None, None, None, prop)
    print(html.props_to_html())

main()
