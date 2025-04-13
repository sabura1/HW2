import unittest
from main import search_text


class TestAhoCorasick(unittest.TestCase):

    def setUp(self):
        self.keywords = ["cat", "dog", "cow", "cattle", "dog house", "cat is"]

    def test_search_basic(self):
        text = "undercattle"
        result = search_text(text, self.keywords)
        expected = {
            "cat": [5],
            "dog": [],
            "cow": [],
            "cattle": [5],
            "dog house": [],
            "cat is": []
        }
        self.assertEqual(result, expected)

    def test_search_no_matches(self):
        text = "xyzabc"
        result = search_text(text, self.keywords)
        expected = {
            "cat": [],
            "dog": [],
            "cow": [],
            "cattle": [],
            "dog house": [],
            "cat is": []
        }
        self.assertEqual(result, expected)

    def test_search_multiple_matches(self):
        text = "cowdogcattle"
        result = search_text(text, self.keywords)
        expected = {
            "cat": [6],
            "dog": [3],
            "cow": [0],
            "cattle": [6],
            "dog house": [],
            "cat is": []
        }
        self.assertEqual(result, expected)

    def test_search_empty_text(self):
        text = ""
        result = search_text(text, self.keywords)
        expected = {
            "cat": [],
            "dog": [],
            "cow": [],
            "cattle": [],
            "dog house": [],
            "cat is": []
        }
        self.assertEqual(result, expected)

    def test_search_patterns_in_text(self):
        text = "cat is in the dog house near the cattle"
        result = search_text(text, self.keywords)
        expected = {
            "cat": [0, 33],
            "cat is": [0],
            "dog": [14],
            "dog house": [14],
            "cow": [],
            "cattle": [33]
        }
        self.assertEqual(result, expected)

    def test_search_overlapping_patterns(self):
        keywords = ["xy", "yz", "xyz"]
        text = "xyzxyz"
        result = search_text(text, keywords)
        expected = {
            "xy": [0, 3],
            "yz": [1, 4],
            "xyz": [0, 3]
        }
        self.assertEqual(result, expected)

    def test_search_with_special_characters(self):
        keywords = ["cat", "dog", "cow", "cattle", "hello"]
        text = "hello! the cat ran past the cattle quietly."
        result = search_text(text, keywords)
        expected = {
            "hello": [0],
            "cat": [11, 28],
            "dog": [],
            "cow": [],
            "cattle": [28]
        }
        self.assertEqual(result, expected)

    def test_search_duplicate_patterns(self):
        keywords = ["dog", "dog", "cow"]
        text = "dogcow"
        result = search_text(text, keywords)
        expected = {
            "dog": [0, 0],
            "cow": [3],
        }
        self.assertEqual(result, expected)

    def test_empty_text(self):
        keywords = ["dog", "dog", "cow"]
        text = ""
        result = search_text(text, keywords)
        expected = {
            "dog": [],
            "cow": [],
        }
        self.assertEqual(result, expected)

    def test_empty_keywords(self):
        keywords = []
        text = "anytext"
        result = search_text(text, keywords)
        expected = {}
        self.assertEqual(result, expected)

    def test_empty_text_and_empty_keywords(self):
        keywords = []
        text = ""
        result = search_text(text, keywords)
        expected = {}
        self.assertEqual(result, expected)