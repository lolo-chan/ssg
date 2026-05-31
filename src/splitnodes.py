from textnode import TextNode, TextType

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

