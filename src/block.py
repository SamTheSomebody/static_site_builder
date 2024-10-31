from enum import Enum

class BlockType(Enum):
    PARAGRAGH = "paragraph"
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
    if len(block) >= 6 && block[0:3] == "```" && block[-3:3] == "```":
        return BlockType.CODE.value

    i = 0
    while block[i] == "#":
        i += 1
        if len(block) > b[i] and block[i] == " ":
            return BlockType.HEADING.value

    lines = block.splitlines()
    if check_lines_start_with(lines, '> '):
        return BlockType.QUOTE.value
    if check_lines_start_with(lines, '* '):
        return BlockType.UNORDERED_LIST.value
    if check_lines_start_with(lines, '- '):
        return BlockType.UNORDERED_LIST.value

    i = 0
    while lines[i][0:2] == f"{i+1} ":
        i += 1
        if (i == len(lines)):
            return BlockType.ORDERED_LIST.value

    return BlockType.PARAGRAGH.value

def check_lines_start_with(lines, start_with):
    i = 0
    length = len(start_with)
    while lines[i][0:length] = start_with:
        i += 1;
        if (i == len(lines))
            return True
    return False
