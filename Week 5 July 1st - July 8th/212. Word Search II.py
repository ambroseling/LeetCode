class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word):
        cur = self  # root node is the self node
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True  # Mark the end of a word
# Time complexity: O(m*n * 4*L) 
# m*n is # of cells in the matrix,  
# In the worst case, each cell in the board is visited, and for each cell, 
# the DFS traversal might explore up to 4 directions. 
# The total number of DFS calls is bounded by the number of cells, (m*n)
# so If a word has length L, each DFS call can explore up to 4 branches for each character, resulting in 
# 4 𝐿 combinations in the worst case.


# Space complexity: The Trie can have at most L nods, where L is the number of characters in the total # of characters in all the words
# Therefore space complexity of the Trie is O(L)
# The recursion stack can go as deep as the longest word length k in the worst case, the visit set uses O(m*n) space
# Therefore total space complexity is: O(L + m*n) 




# these are GPT generated, I didn;t understand this that well, going to review it next week again
class Solution(object):
    def findWords(self, board, words):
        """
        Intuition:
        1. Use a Trie (prefix tree) to efficiently store and look up words from the list.
        2. Traverse each cell on the board and use Depth-First Search (DFS) to explore all possible words starting from that cell.
        3. Use a set to keep track of visited cells during the DFS to avoid revisiting them in the same path.
        4. If a complete word is found in the Trie during DFS traversal, add it to the result set.
        5. Use a set to store the result words to avoid duplicates and convert it to a list at the end.
        """
        root = TrieNode()
        for w in words:
            root.addWord(w)  # Add each word to the Trie

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()  # Initialize result set and visited set

        def dfs(r, c, node, word):
            """
            Depth-First Search to find words in the board.
            
            :param r: Current row index
            :param c: Current column index
            :param node: Current Trie node
            :param word: Current word formed
            """
            # Check if the current position is out of bounds or already visited
            if (r < 0 or c < 0 or r == ROWS or 
                c == COLS or (r, c) in visit or 
                board[r][c] not in node.children):
                return

            visit.add((r, c))  # Mark the current cell as visited
            node = node.children[board[r][c]]  # Move to the child node in the Trie
            word += board[r][c]  # Add the current letter to the word

            if node.word:  # If a complete word is found in the Trie
                res.add(word)

            # Explore the four possible directions (up, down, left, right)
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visit.remove((r, c))  # Unmark the current cell as visited

        # Traverse each cell in the board to start DFS
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)  # Convert the result set to a list and return
