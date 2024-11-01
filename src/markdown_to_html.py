from markdown_block import *
from htmlnode import *
from block_text_to_text_node import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        tag = get_tag_from_block_type(block_type)
        text_nodes = text_to_textnodes(block) #do I need to split the lines for this? Probably also need to clean the tag from the text
        lines = block.splitlines()
        for line in lines:
            #ordered list need addition <li> tags for children
            #assign children to HTML Node (think bold, italic etc.)
        node = HTMLNode(text_nodes)
        #create html node from block type
        #code needs a parent node with a <pre> tag
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

def __create_code_html_nodes__():
    node = ParentNode("pre", code)
    return Node
