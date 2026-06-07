from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.HEADING
    if block.startswith('```\n') and block.endswith('```'):
        return BlockType.CODE
    if block.startswith('>'):
        check = False
        lines = block.split('\n')
        for i in lines:
            if i[0] == '>':
                check = True
            else:
                check = False
        if check:
            return BlockType.QUOTE
    if block.startswith('- '):
        check = False
        lines = block.split('\n')
        for i in lines:
            if i.startswith('- '):
                check = True
            else:
                check = False
        if check:
            return BlockType.UNORDERED_LIST
    if block.startswith('1. '):
        check = False
        lines = block.split('\n')
        for i in range(1, len(lines)+1):
            if lines[i-1].startswith(f'{i}. '):
                check = True
            else:
                check = False
        if check:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

