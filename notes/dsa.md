## Data Structures and Algorithms Notes:

### Big O Notation

### Masters Algorithm


### Sorting

### Binary Trees
* Ways to do traversal:
    - In order
    - Pre-order
    - Post-order
    - Level-order (BFS)
* Binary Search Tree:
    - each node has L and R child, L is always less than self, R is always greater than self
    - 

### Stacks

### Heaps
- complete binary tree that satisfies heap property
- 2 types: Max heap or min heap
- Operations:
    - insert
    - extract
    - heapify
- Binary heap:
    - represented as array
    - `Arr[(i-1)/2]`: parent node
    - `Arr[(2*i)+1]`: left child node
    - `Arr[(2*i)+2]`: right child node

### Priority Queues

### Sliding Window 
- a method that is used to solve problems by defining a **winodw** or range in the input data
- keep a k sized subarray through using a L and R pointer
- Fixed Size Sliding Window
    - Problem Structure: usually are given a window of size k
        - find the size of the window required
        - find result of the window (sum or average or max or whatever)
        - slide the window by 1 (subtract L pointer value, add R pointer value)

- Variabel Size Sliding Window
    - Problem Structure: max or min subarray with some condition (largest sum, repeating/non-repeating characters)
        - Increase right pointer by one till our condition is true
        - If at any point our condition doesn't match, shrink the size of our window by increasing left pointer

### Hash Maps
- Hashing is used to store and retrieve data efficiently using a **hashing function**
    - Hash function: 
        - gets you the data items into the hash function
        - Input: a key, Output: a index into hash table
        - Common hash functions:
            - Division: `key % table_size`
            - Multiplication: `(key * constant) % table_size`
    - Hash code: The hash function crunches the data and give a unique hash code, usually some integer
    - Hash table: 
- In python: 
    - hash maps are implemented as dictionaries
    - note that dictionaries, lists, sets are not hashable, since they are inherently mutable
    -  
     
### Depth First Search
- Explores as far down a branch as possible before backtracking
- Common problems:
    - finding connected components in an undirected graph
    - detecting cycles in a graph
    - topological sorting of a DAG
    - solving maze grid problems (find all paths from start to end)
```python
def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

```
### Breadth First Search
- Explores nodes level by level
- Steps:    
    - dequeue a node from queue and visit it
    - for each unvisited neighbour of the dequeued node 
        - enqueue the neighbour into queue
        - mark neighbour as visited
    - repeat until queue is empty
- Common problems:
    - Finding the shortest path in an unweighted graph (e.g. shortest path in a maze)
    - checking bipartiteness of a graph
    - 
```python
queue = []
visited = [node]
while queue:
    node = queue.pop(0)
    for neighbour in node:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
```

### Dijkstras algorithm