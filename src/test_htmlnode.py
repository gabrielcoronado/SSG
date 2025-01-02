import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        # Test with attributes in props
        node = HTMLNode(tag="a", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

        # Test with empty props
        node_no_props = HTMLNode(tag="div")
        self.assertEqual(node_no_props.props_to_html(), "")

    def test_constructor(self):
        # Test default constructor values
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

        # Test explicit values
        children = [HTMLNode(tag="span"), HTMLNode(tag="p")]
        node = HTMLNode(tag="div", value="Parent", children=children, props={"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Parent")
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, {"class": "container"})

    def test_repr(self):
        # Test the __repr__ method
        node = HTMLNode(tag="p", value="Hello", props={"class": "text"})
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=Hello, children=[], props={'class': 'text'})")


if __name__ == "__main__":
    unittest.main()
