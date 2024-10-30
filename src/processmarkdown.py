import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL.value:
            nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(0, len(split_text)-1, 2):
            if split_text[i] != "":
                nodes.append(TextNode(split_text[i], TextType.NORMAL))
            if split_text[i+1] != "":
                nodes.append(TextNode(split_text[i+1], text_type))
        nodes.append(TextNode(split_text[-1], TextType.NORMAL))
    return nodes

def split_nodes_images(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL.value:
            nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) > 0:
            nodes.extend(split_node_image(node.text, images, 0))
        else:
            nodes.append(node)
    return nodes

def split_node_image(text, images, index):
    nodes = []
    image = images[index]
    split_text = text.split(f"![{image[0]}]({image[1]})")
    if split_text[0] != "":
        nodes.append(TextNode(split_text[0], TextType.NORMAL))
    nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
    if index < len(images) - 1:
        nodes.extend(split_node_image(split_text[1], images, index + 1))
    elif split_text[1] != "":
        nodes.append(TextNode(split_text[1], TextType.NORMAL))
    return nodes

def split_nodes_links(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL.value:
            nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) > 0:
            nodes.extend(split_node_link(node.text, links, 0))
        else:
            nodes.append(node)
    return nodes

def split_node_link(text, links, index):
    nodes = []
    link = links[index]
    split_text = text.split(f"[{link[0]}]({link[1]})")
    if split_text[0] != "":
        nodes.append(TextNode(split_text[0], TextType.NORMAL))
    nodes.append(TextNode(link[0], TextType.LINK, link[1]))
    if index < len(links) - 1:
        nodes.extend(split_node_link(split_text[1], links, index + 1))
    elif split_text[1] != "":
        nodes.append(TextNode(split_text[1], TextType.NORMAL))
    return nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes
