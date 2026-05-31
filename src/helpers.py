from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for i in old_nodes:
        if i.text_type != TextType.TEXT:
            new_nodes.append(i)
        else:
            if delimiter in i.text:
                if i.text.count(delimiter)%2 != 0:
                    raise Exception("no closing delimiter")
                text = i.text.split(delimiter)
                odd = True
                for node in text:
                    if node != '':
                        if odd:
                            new_nodes.append(TextNode(node, TextType.TEXT))
                        else:
                            new_nodes.append(TextNode(node, text_type))
                    odd = not odd
    return new_nodes


def extract_markdown_images(text):
    alt_text = re.findall(r"!\[(.*?)\]", text)
    urls = re.findall(r"\((.*?)\)", text)
    result = []
    for i in range(len(alt_text)):
        result.append((alt_text[i], urls[i]))
    return result


def extract_markdown_links(text):
    anchor_text = re.findall(r"\[(.*?)\]", text)
    urls = re.findall(r"\((.*?)\)", text)
    result = []
    for i in range(len(anchor_text)):
        result.append((anchor_text[i], urls[i]))
    return result


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        text = node.text
        for i in images:
            sections = text.split(f"![{i[0]}]({i[1]})", 1)
            if sections[0] != '':
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(i[0], TextType.IMAGE, i[1]))
            text = sections[1]
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_links(node.text)
        text = node.text
        for i in images:
            sections = text.split(f"[{i[0]}]({i[1]})", 1)
            if sections[0] != '':
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(i[0], TextType.LINK, i[1]))
            text = sections[1]
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

