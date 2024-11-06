## Data Structures and Algorithms Notes:

> Some log laws:
> $\log A^n = n log A$
> $\log A + \log B = \log A B$
> $\log \frac{A}{B} = \log A - \log B$
> $a^{\log b} = b ^{log a}$


### Big O Notation
- $\Omega$ - notation
    - when we only have an **asymptotic lower bound** for $f(n)$
    - For a given function $g(n)$, we denote by $O(g(n))$ the set of functions
    $$
    \Omega(g(n)) = \{f(n): \text{There exists **some** positive constants } c \text{ and } n_0 \text{ such that } 0 \lt c g(n) \lt f(n) \text{ for all } n \geq n_0\}
    $$
- $O$ - notation
    - when we only have an **asymptotic upper bound** for $f(n)$
    - For a given function $g(n)$, we denote by $O(g(n))$ the set of functions
    $$
    \Omega(g(n)) = \{f(n): \text{There exists **some** positive constants } c \text{ and } n_0 \text{ such that } 0 \lt f(n) \lt c g(n)\}
    $$ 
- $\Theta$ - notation
    - wrost case running time
    - when we have an **asymptotically tight bound** for $f(n)$
    - For a given function $g(n)$, we denote by $\Theta(n^2)$ the set of functions 
    $$
    \Omega(g(n)) = \{f(n): \text{There exists positive constants } c_1, c_2, \text{ and } n_0 \text{ such that } 0 \lt c_1 g(n) \lt f(n) \lt c_2 g(n)\}
    $$

- $o$ - notation
    - For a given function $f(n)$, we define $o(g(n))$ as the set $o(g(n)) = \{ f(n) : \text{for **any** positive constant } c \gt 0, \text{ there exists a constant } n_0 \gt 0 \text{ such that } c g(n) \text{ for all } n \geq n_0\}$ 
    - can also be defined by the limit $\lim_{n \rightarrow \infty} \frac{f(n)}{g(n)} = 0$
- $\omega$ - notation
    - For a given function $f(n)$, we define $\omega(g(n))$ as the set $o(g(n)) = \{ f(n) : \text{for **any** positive constant } c \gt 0, \text{ there exists a constant } n_0 \gt 0 \text{ such that } 0 \leq c g(n) \lt f(n) \text{ for all } n \geq n_0\}$ 
    - can also be defined by the limit $\lim_{n \rightarrow \infty} \frac{f(n)}{g(n)} = \infty$ 

### Masters Algorithm
- Let $a \geq 1$  and $b \gt 1$ be constants, let $f(n)$ be a function and let $T(n)$ be defined on the nonnegative integers by the recurrence $T(n) = a T(n/b) + f(n) $ where we interpret $n/b$ to mean either $\lfloor n/b \rfloor$ or $\lceil n/b \rceil$ 
    - 1. if $f(n) = O(n^{log_b(a)- \epsilon})$ for some constant $\epsilon \gt  0$ , then $T(n) = \Theta(n^{log_b(a)})$
    - 2. if $f(n) = O(n^{log_b(a )})$, then $T(n) = \Theta(n^{log_b(a)} lg n)$
    - 3. if $f(n) = \Omega(n^{log_b(a) + \epsilon})$ for some constant $\epsilon \gt  0$ , and if $af(n/b) \leq cf(n)$ for some constant $c \lt 1$ and all sufficient large n, then $T(n)  = \Theta(f(n))$
- Very important lemma:
    - we can prove with a recursion tree
        - $T(n) = \{\Theta(n) \text{ if } n = 1, a T(n/b) + f(n) \text{ if } n = b^i\}$
        - where $i$ is a positive integer then 
        - $T(n) = \Theta(n^{log_b(a)}) + \Sigma_{j=0}^{log_b(n-1) a_j f(n/b^j)}$
    - 3 cases of masters theorem correspond to 
- For uneven recurrences:
    - https://cs.stackexchange.com/questions/79781/run-time-of-recurrence-with-five-uneven-calls
### Recurrences:
- Method 1:  Substitution Method
    - guess a bound, use mathematical induction to prove our guess is correct
    - converts a recurrent into a tree (use techniques of bounding summations)
    - master method for recurrneces of the form $T(n) = aT(n/b)  + f(n) $
    - Example: assume we have the recurrence $T(n) = 2T(\\lfloor n/2 \rfloor) + n$
        - we make the assumption $T(n) = O(nlgn)$, we substitue the recurrence inside $T(\lfloor n/2 \rfloor) \leq c \lfloor n/2 \rfloor lg(\lfloor n/2 \rfloor)$
        - We get:
    $$
    T(n) \leq 2(c \lfloor n/2 \rfloor lg(\lfloor n/2 \rfloor)) + n \\
    T(n) \leq c n lg(n/2) + n \\ 
    T(n) =  cnlgn - cnlg2  + n \\
    T(n) = cnlgn - cn + n \\ 
    T(n) \leq cnlgn
    $$
    - We provide an inductive hypothesis that $T(n) \leq c n lg n$ for $n \geq n_0$
- Method 3: Masters theorem see above
### Sorting
- Merge Sort:
    - Recurrence equation: $T(n) = \{ \Theta(1) \text{ if } n = 1, 2T(n/2) + \Theta(n) \text{ if } n \gt 1\}$
```python
def merge(arr,left,mid,right):
    l = arr[left:mid+1]
    r = arr[mid+1:right]
    i = 0
    j = 0
    k = left
    while i < mid - left + 1 and j < right - mid:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i+=1
        else:
            arr[k] = r[j]
            j+=1
        k+=1
    while i < mid - left + 1:
        arr[k] = l[i]
        i+=1
        k+=1
    while j < right - mid:
        arr[k] = r[j]
        j+=1
        k+=1

def merge_sort(arr,left,right):
    if left < rightL:
        mid = (left + right) //2 
        merge_sort(arr,left,mid)
        merge_sort(arr,mid+1,right)
        merge(arr,left,mid,right)
```
- Quick Sort:
    - Recurrence equation: $T(n) = $
```python
# Function to find the partition position
def partition(array, low, high):

    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)

```

- Heap Sort:
    - You maintain a heap
    ```python
    def max_heapify(array,n,i):
        index = i
        if 2*i < n and array[2*i] < array[2*i+1]:
            index = 2*i
        elif 2*i+1 < n and array[2*i] > array[2*i+1] :
            index = 2*i+1
        
        if index != i:
            array[i],array[index] = array[index],array[i]
            max_heapify(array,n,index)

    def extract_max(array):
        array[0],array[-1] = array[-1],array[0]
        max_heapify(array,n,i)

    def heapsort(array,n):
        #build the heap
        build_max_heap(array)

        # iterate through every node
        for i in range(n-1,0,-1):
            # at every iteration you extract the maximum element 
            array[i],array[-1] = array[-1],array[i]

            max_heapify(array,i,0)
    ```
### Probabilistic Analysis
- Algo is randomized if behvaiour is determined by input + values from random value generator
- Hire Assistant example:
    - Problem statement:
        - you can interview a candidate and decide to hire them or not
        - you need to fire candidate and hire candidate (hiring has cost)
        - $X_i = I \{ \text{ candidate i is hired}\} = \{1 \text{ if candidate i is hired }, 0 \text{ 0 if candidate is not hired} \}$
        - $X = X_1 + X_2 + X_3 ... + X_n$
    ```python
    best = 0
    for i in range(n):
        #interview candidates i
        if candidate i better than candidate best:
            best = i
            hire candidates i
    ```
    - Assumptions:
        - Hiring cost: $c_h$
        - Interview cost: `` $c_i$
    - Big O time complexity: $O(c_i n + c_h m)$
    - Worst case time complexity: $O(c_h m)$
- Indicator Random Variables
    - Indicator random variable $I \{A\}$ associated with event A is defined as:
    - $I \{A\} = \{1 \text{ if A occurs }, 0 \text{ if A does not occur}\}$
    - Lemma 5.1: Given a sample space S and event A in the sample space S, let $X_A = I\{A\}$, then $E[X_A] = Pr\{A\}$


### Trees
Definitions
1. A tree is an undirected graph in which any 2 vertices are connected with exactly one path
2. Any connected graph who has n nodes with n-1 edges is a tree
3. The degree of a vertex of a graph is the number of edges incident of the vertex
4. A leaf is a vertex of degree 1 
5. A path graph is a tree with 2 or more vertices that is not branched at all
6. A tree is called a rooted tree if one vertex has been designated
7. the height of a tree is the number of edges that form the longest path from root to leaf

### Binary Trees

* Ways to do traversal:
    - In order (Left Root Right)
        - used for sorting
    - Pre-order (Root Left Right)
        - used for rotation
    - Post-order (Left Right Root)
        - used for deleting
    - Level-order (BFS)

* Binary Search Tree:
    - each node has L and R child, L is always less than self, R is always greater than self
    - if a Binary Search Tree has n nodes, h = O(n)
    - Only if the BST is balanced, h = O(log(n))
* Finding the minimum:
```python
def minimum(x):
    while x.left != None:
        x = x.left
    return x
```
* Finding the maximum:
```python
def maximum(x):
    while x.right != None:
        x = x.right
    return x
```
* Finding predecessor (the element right before it):
```python
def predecessor(x):
    if x.left != None:
        return maximum(x):
    y = parent(x)
    while y != None and x == y.right:
        x = y
        y = parent(y)
    return y
```
* Finding Sucecssor (the element right after it):
```python
def successor(x):
    if x.right != None:
        return minimum(x)
    y = parent(x)
    while y != None and x == y.left:
        x = y
        y = parent(y)
```
* Search
```python
def search(x,k):
    if x == None or x.key == k:
        return x
    if x.key > k:
        search(x.left,k)
    if x.key < k:
        search(x.right,k)
```

* Insert
```python
def insert(root,z):
    y = None, x = root
    while x != None:
        y = x # find where z should connect
        # if value you want to insert is smaller than current node
        if z.key < x.key:
            # go left
            x = x.left
        # if value you want to insert is greater than current node
        else:
            # go right
            x = x.right
    
    # parent of the node we want to insert is set to y
    parent(z) = y
    # if 
    if y == None:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
```
* Delete 
```python
def delete():

```
- Case 1:
    - 
- Case 2:
    - 
- Case 3:
    -  
### Red Black Trees


### Stacks


### Queues
#### Circular Queues:



### Heaps
- complete binary tree that satisfies heap property
- 2 types: Max heap or min heap
- Heap property:
    - Max heap: $A[Parent[i]] \geq A[i]$
    - Min heap: $A[Parent[i]] \leq A[i]$
- Operations:
    - insert
    - extract
    - heapify
- Binary heap:
    - represented as array
    - `Arr[floor((i-1)/2)]`: parent node
    - `Arr[(2*i)+1]`: left child node
    - `Arr[(2*i)+2]`: right child node
- Heapify:
    - Recurrence is bounded by $T(n) \leq T(2n/3) + \Theta(1)$
```python
# Method 1:
def heapify(arr,n,i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if (l < n and arr[l] > arr[largest]): #if the left is larger than the current root
        largest = l
    if (r < n and arr[r] > arr[largest]): #if the right is larger than the current root
        largest = r
    if (largest != i): #if the largest isnt the root
        arr[i] , arr[largest] = arr[largest], arr[i]
        heapify(arr,n,largest)

# Method 2: 
def heapify(arr,n,i):
    parent = int((i-1)/2)
    if parent >= 0:
        if arr[i] > arr[parent]:
            arr[i],arr[parent] = arr[parent],arr[i]
            heapify(arr,n,parent)


```
- Heap insertion:
```python
def insert(arr,key):
    n += 1
    arr.append(key)
    heapify(arr,n,n-1)
```
- Heap deletion:
```python
def delete(arr):
    arr[0]  = arr[n-1]
    n = n-1
    heapify(arr,n,0)
```
- Heap view:
```python
def view(arr)
    return arr[0]
```
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

### Greedy Algorithms
* make locally optimal decisions at each steo, locked in and never revisited later
* Greedy choice property:
    * there is an optimal solution that agrees with the first greedy choice the algorithm makes.
* Inductive Proof of optimality:
    - Make the first greedy choice on problem (call it $P_n$), reducing the problem to a smaller subproblem (call it $P_{n-1}$)
    - there is an optimal solution to $P_n$ that agrees with this choice by the greedy choice property.
    - recursively solve the smaller subproblem $P_{n-1}$ to get a solution $S_{n-1}$  
    - By optimal substructure, if $S_{n-1}$ is optimal, adding the greedy choice to it yields an optimal solution to $P_n$.
    - Since $P_{n-1}$ is the same type of problem as $P_n$, it also has the greedy choice property
    - Make the first greedy choice for $P_{n-1}$, it agrees with an optimal solution to $P_{n-1}$ and reduces the problem to a smaller subproblem $P_{n-2}$
    - Repeat until there is no smaller subproblem


### Dynamic Programming
 FAST method:
 1. First Solution
 2. Analyze the first solution
 3. Identify the subproblems
 4. Turn the solution around
 