Counting Sort:
- assumes elements are integers ranging from 0 to k
- Runtime: Theta(n + k)  if k = Theta(n) then runtime is Theta(n)
- Counting sort: 
- Counting sort uses no comparisons
- Counting sort is not in place
- Counting sort is stable

```
function CountingSort(A,B,n,k):
    for each i = 0:k do :
        C[i] = 0
    for each j = 1:n do :
        C[A[j]] = C[A[j]] + 1
    for each i = 1:k do:
        C[i] = C[i] + C[i-1]
    for j = n:1 do:
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1
```


Radix Sort:
- assumes all elements have <= d digits
- runtime Theta(d(n+k)) for d digit numbers and each digiit \in [0,k]
- overall, it sorts in Theta(n)
- radix sort uses no comparisons
- radix sort is not in place
- radix sort is stable
- radix sort time complexity: Theta()



How to prove an algorithm is stable?
- 

Lemma: given n bit numbers and any postiive integer r <= b, radix sorts in Theta(b/r(n+2^r)), if stable sort is Theta(n+k)


Sort an array of integers ranging from -100 to 100 in O(n) time
- shift all integers by + 100  O(n)
- sort the array by counting sort O(n+200) = O(n)
- shift output by -100 O(n)
Total time: O(n) 


Given A[i,..,m] with elements of positive integers. Let A[i] have d_i digits and \Sum_{i=1}^{m} d_i = n. Sort A in O(n) time
- Naive solution:
    - let d = max(d_i) that is Theta(n)
    - we call radix sort on d digits (\Theta(d(m+k)))
- 

Sort n integers ranging from 0 to n^3 in O(n) time
- change all the integers to base n
- since n^3 can be represented in the form of a_2 n^2 + a_1 n^1 + a^0 n^0
- os you have 3 digits, and we run radix sort with d= 3, k = n
- O(d(n+k)) = O(3(n+n)) = O(n)


Summary on sorting algos (worst case runtime):
- merge sort: Theta(n log n)
- heap sort: Theta(n log n)
- quick sort: Theta(n^2)
- counting sort: Theta(n+k)
- radix sort: Theta(n^2)


Binary Search Trees:
- BST properties: 
    - if y in left subtree of x, key(y) <= key(x)
    - if y is in right subtree of x, key(y) >= key(x)
- if BST has n nodes, h = O(n).
- Only if te BST is balanced, h = O(logn)
- minimum / maximum and searching for any arbitrary key O(h)
- successor / predecessor O(h)
- insertion/deletion O(h)
- build BST O(n^2) worst case

