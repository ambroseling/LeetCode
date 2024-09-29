class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1: return [0] 
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1] # get all the leave nodes of the tree
        while n > 2:
            n -= len(leaves) # take away all the leaves then get the size of the tree 
            newLeaves = []
            for i in leaves: # go through all the leaves
                j = adj[i].pop() # get their neighbours
                adj[j].remove(i) # remove the source node (so you dont visit that again)
                if len(adj[j]) == 1: newLeaves.append(j) #if its neighbour is a leaf add it to the newLeaves
            leaves = newLeaves # set that as your new leaves

        return leaves

	
# Runtime : 104ms
# The idea is to eat up all the leaves at the same time until you reach the root
