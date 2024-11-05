from markdown_blocks import *
from html_node import *
from inline_markdown import text_to_text_nodes
from text_node import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        node = __block_to_html_node__(block)
        children.append(node)
    return ParentNode("div", children)

def __block_to_html_node__(block):  
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return ordered_list_to_html_node(block) 
        case BlockType.CODE:
            return code_to_html_node(block) 
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
    raise ValueError("Invalid Block Type!")

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    children = list(map(lambda x: text_node_to_html_node(x), text_nodes))
    return children

def paragraph_to_html_node(block):
    children = text_to_children(block)
    return ParentNode("p", children)

def heading_to_html_node(block):
    split = block.split(" ")
    length = len(split[0])
    value = " ".join(split[1:])
    children = text_to_children(value)
    return ParentNode(f"h{length}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    node = ParentNode("code", children)
    return ParentNode("pre", [node])

def ordered_list_to_html_node(block):
    lines = block.splitlines()
    func = lambda x: (ParentNode("li", text_to_children(x[3:])))
    children = list(map(func, lines))
    return ParentNode("ol", children)

def unordered_list_to_html_node(block):
    lines = block.splitlines()
    func = lambda x: ParentNode("li", text_to_children(x[2:]))
    children = list(map(func, lines))
    return ParentNode("ul", children)

def quote_to_html_node(block):
    lines = block.splitlines()
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)
