class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()



    def addWord(self, word):
        cur = self.root
        for c in word: 
            # if we dont already have the character under cur
            if c not in cur.children:
                cur.children[c] = TrieNode() # make the node
            # if we do have it, we simply shift over to it
            cur = cur.children[c]
        # Finally, mark the last character as end of the word 
        cur.word = True
    
    def search(self, word):
        ''' intuition:  
            we have the "." to worry about, so when that happens we simply 
            call the dfs and it takes care of it.
        '''
        def dfs(j, root):
            # set the current pointer to root node.
            cur = root
            # for each character in range j, to end of word. 
            # we do j, as it keeps track of the past iterations of the dfs we have looked over
            # and helps us account for the "." as we can just check the next character after "."
            # This is why we DON'T do for c in word:
            for i in range(j, len(word)):
                # c is the next character
                c = word[i]
                # when we have the period, meaning it can be any of the characters.
                if c == ".":
                    # so we say for ALL the children of the cur node, we loop through and see if any of them returns True
                    for child in cur.children.values():
                        if dfs(i + 1, child): # if the dfs finds a word, then we good
                            return True
                    return False # or else return the False if none of cur.children have a viable path
                else:
                    # if that character doesn't exist, return False
                    if c not in cur.children:
                        return False
                    # if it exists, just shift cur pointer to next node
                    cur = cur.children[c]
            return cur.word # if the last char is marked as being end of word or not.
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)