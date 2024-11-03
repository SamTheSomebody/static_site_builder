from markdown_block import *
from htmlnode import *
from block_text_to_text_node import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        tag = get_tag_from_block_type(block_type)
        lines = block.splitlines()
        if tag == "ol":
            for i in range(0, len(lines)):
                lines[i] = f"<li>{line}</li>"
        cleaned_block = __remove_markdown_block_tags__(block, block_type)
        text_nodes = text_to_textnodes(cleaned_block)
        child_nodes = list(map(lambda x: text_node_to_html_node(x), text_nodes))
        node = ParentNode(tag, child_nodes)
        if tag == "code":
            node = ParentNode("pre", node)
        children.append(node)
    return ParentNode("div", children)

def __get_tag_from_block_type__(block, block_type):
    match block_type:
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.UNORDERED_LIST:
            return "ul"
        case BlockType.ORDERED_LIST:
            return "ol"
        case BlockType.CODE:
            return "code"
        case BlockType.HEADING:
            return f"h{len(block.split(" ")[0])}"
        case _:
            return "p"

def __remove_markdown_block_tags__(block, block_type):
    match block_type:
        case BlockType.QUOTE:
            return __remove_start_of_lines(block, 2)
        case BlockType.UNORDERED_LIST:
            return __remove_start_of_lines(block, 2)
        case BlockType.ORDERED_LIST:
            return __remove_start_of_lines(block, 3)
        case BlockType.CODE:
            return block[3:len(block)-6]
        case BlockType.HEADING:
            return (" ").join(block.split(" ")[1:])
        case _:
            return block

def __remove_start_of_lines(block, length):
    lines = block.splitlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i][:length)
    return ("\n").join(lines)


