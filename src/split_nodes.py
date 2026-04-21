from textnode import TextType, TextNode
from extract_markdown_images import extract_markdown_images
from extract_markdown_links import extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        count = original_text.count(delimiter)
        if count % 2 != 0:
            raise Exception("Invalid Markdown syntax")

        texts = original_text.split(delimiter)
        for i in range(len(texts)):
            if i % 2 != 0:
                new_nodes.append(TextNode(texts[i], text_type))
            else:
                new_nodes.append(TextNode(texts[i], TextType.TEXT))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if old_node.text_type is not TextType.TEXT or len(images) == 0:
            new_nodes.append(old_node)
            continue

        current_text = original_text
        for image in images:
            image_alt = image[0]
            image_url = image[1]

            sections = current_text.split(f"![{image_alt}]({image_url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid Markdown: Image Section not found")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

            current_text = sections[1]

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if old_node.text_type is not TextType.TEXT or len(links) == 0:
            new_nodes.append(old_node)
            continue

        current_text = original_text
        for link in links:
            link_alt = link[0]
            link_url = link[1]

            sections = current_text.split(f"[{link_alt}]({link_url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid Markdown: Link Section not found")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))

            current_text = sections[1]

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes
