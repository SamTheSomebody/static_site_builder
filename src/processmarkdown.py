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
