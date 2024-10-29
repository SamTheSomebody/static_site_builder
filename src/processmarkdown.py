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


def extract_markdown_images(text):
    extracted_images = []
    if "!" not in text:
        return extracted_images

    regex = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    print(regex)

    images = text.split('!')
    for image in images[1:]:
        alt_text = re.findall(r"\[(.*?)\]", image)
        href = re.findall(r"\((.*?)\)", image)
        extracted_images.append((alt_text[0], href[0]))
    return extracted_images
