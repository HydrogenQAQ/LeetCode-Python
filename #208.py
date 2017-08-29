# -*- coding: utf-8 -*-

"""
@author: Jinqf
@file: #208
@time: 2017/8/28 8:57
字典树：
--------根节点不包含字符，除根节点外每一个节点都包含字符
--------从根节点到某一个节点，路径上所有的字符连接起来为该节点对应的字符串
--------每个节点的所有子节点包含的字符串不同
"""


class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for x in word:
            if x not in node:
                node.children[x] = TrieNode()
            node = node.children[x]
        node.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for x in word:
            if x not in node:
                return False
            node = node.children[x]
        return node.word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for x in prefix:
            if x not in node:
                return False
            node = node.children[x]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)