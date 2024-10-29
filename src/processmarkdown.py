from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL.value:
            nodes.append(node)
            continue
        if delimiter not in node.text:
            raise ValueError(f"'{delimiter}' not found in '{node.text}'")
        split_text = node.text.split(delimiter)
        for i in range(0, len(split_text)-1, 2):
            nodes.append(TextNode(split_text[i], TextType.NORMAL))
            nodes.append(TextNode(split_text[i+1], text_type))
        nodes.append(TextNode(split_text[-1], TextType.NORMAL))
    return nodes
