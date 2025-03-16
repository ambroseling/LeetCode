class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        # setting our pointer to first root node. (which is empty always)
        cur = self.root
        # now iterating over all characters in the word:
        for c in word:
            # if we dont have that character, we make a new node, as a child
            if c not in cur.children:
                # initialize the node + saving the child as for the parent.
                cur.children[c] = TrieNode()
            # move the pointer to the next character,
            cur = cur.children[c]
        # finally, we mark the end node as EndOfWord
        cur.endOfWord = True

    def search(self, word):
        cur = self.root
        for c in word: 
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix: 
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)