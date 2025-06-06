import unittest
from lab_7 import Trie, build_trie  # Замініть на реальну назву модуля

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.patterns = ["cat", "cap", "can", "dog", "door"]
        self.trie = build_trie(self.patterns)

    def test_search_existing_words(self):
        self.assertTrue(self.trie.search("cat"))
        self.assertTrue(self.trie.search("cap"))
        self.assertTrue(self.trie.search("can"))
        self.assertTrue(self.trie.search("dog"))
        self.assertTrue(self.trie.search("door"))

    def test_search_non_existing_words(self):
        self.assertFalse(self.trie.search("car"))
        self.assertFalse(self.trie.search("do"))
        self.assertFalse(self.trie.search(""))

    def test_starts_with_valid_prefixes(self):
        self.assertTrue(self.trie.starts_with("ca"))
        self.assertTrue(self.trie.starts_with("do"))
        self.assertTrue(self.trie.starts_with("c"))
        self.assertTrue(self.trie.starts_with("d"))

    def test_starts_with_invalid_prefixes(self):
        self.assertFalse(self.trie.starts_with("du"))
        self.assertFalse(self.trie.starts_with("z"))
        self.assertFalse(self.trie.starts_with("cab"))
        self.assertFalse(self.trie.starts_with("doorway"))

if __name__ == '__main__':
    unittest.main()
