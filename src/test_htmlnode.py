import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("p", "this is the text")
        node2 = HTMLNode("p", "this is the text")
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = HTMLNode("p", "this is the text")
        node2 = HTMLNode("a", "this is not the text")
        self.assertNotEqual(node1, node2)

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node1 = HTMLNode("a", "this is the text", None, props)
        correct_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node1.props_to_html(), correct_result)

    
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")    


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )    
