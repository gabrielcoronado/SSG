import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_constructor_with_url(self):
        node = TextNode("This is a link", TextType.LINKS, "https://example.com")
        self.assertEqual(node.url, "https://example.com")

    def test_not_equal(self):
        node1 = TextNode("This is bold text", TextType.BOLD)
        node2 = TextNode("This is italic text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        self.assertEqual(
            repr(node),
            "TextNode(This is a text node, bold, https://example.com)"
        )


if __name__ == "__main__":
    unittest.main()