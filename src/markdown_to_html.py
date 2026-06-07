from htmlnode import HTMLNode, ParentNode, LeafNode
from helpers import *
from block import block_to_block_type, BlockType
from textnode import *


def blocktype_to_tag(block) -> str:
    match(block_to_block_type(block)):
        case(BlockType.PARAGRAPH):
            return "p"
        case(BlockType.HEADING):
            return f"h{len(block.split(' ')[0])}"
        case(BlockType.CODE):
            return "code"
        case(BlockType.QUOTE):
            return "blockquote"
        case(BlockType.UNORDERED_LIST):
            return "ul"
        case(BlockType.ORDERED_LIST):
            return "ol"
        case _:
            raise Exception("invalid block type")
        

def text_to_children(text: str) -> HTMLNode:
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children


def strip_markdown_syntax(text: str, block_type: BlockType) -> str:
    match(block_type):
        case(BlockType.PARAGRAPH):
            lines = text.split('\n')
            new_text = ' '.join(lines)
            return new_text
        case(BlockType.HEADING):
            return text.split(' ', 1)[1]
        case(BlockType.CODE):
            text = text[3:-3]
            if text.startswith('\n'):
                text = text[1:]
            # if text.endswith('\n'):
                # text = text[:-1]
            return text
        case(BlockType.QUOTE):
            lines = text.split('\n')
            clean_lines = []
            for line in lines:
                if line.startswith('> '):
                    clean_lines.append(line[2:])
                else:
                    clean_lines.append(line[1:])
            new_text = '\n'.join(clean_lines)
            return new_text
        case _:
            return text
        

def process_lists(text: str, block_type: BlockType):
    if block_type == BlockType.UNORDERED_LIST:
        items = text[2:].split('\n- ')
        return [ParentNode("li", text_to_children(item)) for item in items]
    if block_type == BlockType.ORDERED_LIST:
        pre_items = text.split('\n')
        items = [item.split(' ', 1)[1] for item in pre_items]
        return [ParentNode("li", text_to_children(item)) for item in items]
    

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type != BlockType.CODE and block_type != BlockType.ORDERED_LIST and block_type != BlockType.UNORDERED_LIST:
            new_node = ParentNode(blocktype_to_tag(block), text_to_children(strip_markdown_syntax(block, block_type)), None)
            nodes.append(new_node)
        elif block_type == BlockType.CODE:
            new_node = ParentNode("pre", [text_node_to_html_node(TextNode(strip_markdown_syntax(block, BlockType.CODE), TextType.CODE, None))])
            nodes.append(new_node)
        elif block_type == BlockType.UNORDERED_LIST or block_type == BlockType.ORDERED_LIST:
            new_node = ParentNode(blocktype_to_tag(block), process_lists(block, block_type), None)
            nodes.append(new_node)
    return ParentNode("div", nodes, None)
