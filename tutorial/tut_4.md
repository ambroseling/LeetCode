Max heap
- binary tree with the max heap property:
    - for any vertex $v_i$:key(parent(v_i)) > key(v_i)
- To prove that the root of ths subtree contains the largest value occuring anywhere in the subtree:
    - base step: assume a heap with size 1, root is the largest
    - inductive hypothesis: for any heap size 0 <= k <= n
    - 
- heap is an array where node at index i, children are at 2i and 2i + 1 
Heapsort
- has O(nlogn) worst run time
- minimum and maximum number of elements in a heap of height h:
    - maximum when its a complete binary tree:  
        - so there are $2^{h+1} - 1$ elements
    - minimum when the heap has only one node in its lowest level
        - in this case $2^{h} -1 + 1 = 2^h$
            - $2^{h} - 1$ refers to a complete tree of height h -1
- show that n element heap has height ceil(logn):
    - 2^h < n 2^{h+1} - 1 < 2^{h+1}
    - h < lgn < h+1

How to merge k sorted lists:
- Let A denote final sorted list
- Keep the smallest element from each list in a heap H, and augment each element with the index of the list it came from
- Heap stores pairs of the form (x,i) x is a number from the input and i is index of the list it came fmor 
- heap is sorted by x:
- use deleteMin to remove the smallest element from the heap and append to A, then add the next element of list i to H
- Run time analysis:
    - building the heap takes O(k) time
    - heap is always of size k or less, so it takes O(logK) to pop elements
    - O(logK) to readd the next element from the appropriate list
    - done n times for a total of $O(nlogk)$
    - total run time is O(k + n log k) = O(n log k)


Worst case run time of MAX-HEAPIFY is \
- the worst case run time occurs when a swap is necessary at every recursion step down the tree. In that case, we would have to go through every level of the tree. Since the height of the tree is lg(n), 
- consider a max heap where the root is the smallest element and for simplicity
- also assume that when MAX-HEAPIFY is called, the original root will always be swapped with its left child
- the call will only terminate when the original root becomes a leaf, which requires h swaps, that is the length of the leftmost path.
```
def max_heapify(n,i):
    left = A[2i]
    right = A[2i+1]
    if left < right:
        index = 2i
    else:
        index = 2i+1
    if A[i] > A[index]:
        A[i],A[index] = A[index], A[i]
    max_heapify() 
```


Quick sort 
- has O(n^2) worst run time
- recurrence: $T(n) = 2T(n/2) + Theta(n)$
    - this is best case that pivot is chosent to be the median element each time
    - worst:
        - T(n) = T(9n/10) + T(n/10) + Theta(n)