from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = []
    split = markdown.split("\n\n")
    for s in split:
        if s != "":
            blocks.append(s.strip())
    return blocks

def block_to_block_type(block):
    if len(block) == 0:
        raise ValueError("Block is empty!")
    lines = block.splitlines()
    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if check_block_starts_with_heading(lines[0]):
        return BlockType.HEADING
    if check_lines_start_with(lines, '> '):
        return BlockType.QUOTE
    if check_lines_start_with(lines, '* '):
        return BlockType.UNORDERED_LIST
    if check_lines_start_with(lines, '- '):
        return BlockType.UNORDERED_LIST
    if check_lines_start_with_ordered_list(lines):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def check_block_starts_with_heading(line):
    i = 0
    while line[i] == "#" and i < 6:
        i += 1
        if len(line) > i and line[i] == " ":
            return True
    return False

def check_lines_start_with(lines, start_with):
    for line in lines:
        if not line.startswith(start_with):
            return False
    return True

def check_lines_start_with_ordered_list(lines):
    i = 0
    for line in lines:
        i += 1
        if not line.startswith(f"{i}. "):
            return False
    return True
