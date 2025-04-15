import unittest
from main import search_text


class TestAhoCorasick(unittest.TestCase):

    def test1(self):
        text = "hello"
        keywords = []
        result = search_text(text, keywords)
        assert result == {}, f"Test 1 failed"

    def test2(self):
        text = "a"
        keywords = ["b"]
        result = search_text(text, keywords)
        assert result == {"b": []}, f"Test 2 failed"

    def test3(self):
        text = ""
        keywords = ["abc", ""]
        result = search_text(text, keywords)
        assert result == {"abc": [], "": []}, f"Test 3 failed"

    def test4(self):
        text = "abcdefgh"
        keywords = ["ijkl", "mnop"]
        result = search_text(text, keywords)
        assert result == {"ijkl": [], "mnop": []}, f"Test 4 failed"

    def test5(self):
        text = "mississippi"
        keywords = ["mis", "sip", "ss"]
        result = search_text(text, keywords)
        assert result == {"mis": [0], "sip": [6], "ss": [2, 5]}, f"Test 5 failed"

    def test6(self):
        text = "xyz"
        keywords = ["abc"]
        result = search_text(text, keywords)
        assert result == {"abc": []}, f"Test 6 failed"

    def test7(self):
        text = "abcxabcdabxabcdabcdabcy"
        keywords = ["abcd", "abc"]
        result = search_text(text, keywords)
        assert result == {"abc": [0, 4, 11, 15, 19], "abcd": [4, 11, 15]}, f"Test 7 failed"