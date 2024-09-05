# Memoization Receipe
- a solution that is recursive
    - visualize the problem as a tree
    - implement the tree using recursion
    - leaves as your base case
    - test it
- make it efficient
    - add a memo object
    - add a base case to return memo values
    - store return values into the memo

# Fibonacci problems
```python
def fib(n):
    if n <=2 return 
    return fib(n-1) + fib(n-2)
```


Time complexity is `O(2^n)`
Space complexity is `O(n)`


1. foo exmple
```python
def foo(n):
    if n <=1 return 
    foo(n-1)
```

Time complexity is `O(n)`
Space comlexity is `O(n)`

2. bar example
```python
def bar(n):
    if n <=1 return 
    bar(n-2)
```
Time complexity is `O(n)`
Space complexity is `O(n)`


3. 
```python
def dib(n): 
    if (n <= 1): return
    dib(n-1)
    dib(n-1)
```
Height = Num of levels = n
Every time you move donw a level, you multiply by 2, 
hence time complexity is `O(2^n)`

Space complexity: the most stack frames we use up is the height of the tree `O(n)`

4. 
```python
def lib(n):
    if (n <= 1): return
    lib(n-2)
    lib(n-2)
```
Time complexity = `O(2^(n/2))` which is same as `O(2^n)`
Space complexity is `O(n)`

Fib's time complexity falls right in btw dib and lib
```python
def fib(n):
    if n <=2 return 
    return fib(n-1) + fib(n-2)
```
Time complexity of `O(2^n)` is not desirable
fib(50) = 2^50 steps


Memoization:
- store soem duplicate subprobelms and use it later on
- usually use a hash map

```python
def fib(n,memo):
    if n in memo: return memo[n]
    if n <=2 return 1
    memo[n] =  fib(n-1,memo) + fib(n-2,memo)
    return memo[n]
```
By memoizing fib, we cut down time complexity to `O(n)` and `O(n)` space complexity.

# grid Traveller
Say you are a traveller on a 2D grid, you begin in the top left corner and your goal is to travel to teh bottom right corner you may only move down or right

in how many ways can you travel to the goal on a grid with dimensions m*n?

Write a function `gridTraverler(m,n)` that calculates this
example: `gridTraveler(2,3)` -> 3
1. right, right, down
2. right, down , right
3. down, right, right


Bases cases:
- m and n cannot be 0 or would be 0 ways
- if its a 1x1 grid, there is only 1 way

example: `gridTraveler(3,3)` -> 3 
- how to shrink the problem
- once you make a move, you are shorting the problme to how many ways to move in the smaller grid
- keep shrinking problem size

```python
def gridTraveler(m,n):
    if (m == 1 and n == 1) return 1
    if (m == 0 or n == 0) return 0
    return gridTraveler(m-1,n) + gridTraveler(m,n-1)
```
n+m is how many times you need to subtract in order to get to your base case. hence you have n+m levels in your binary tree

Time complexity: `O(2^(n+m))`
Space complexity: `O(n+m)` space

How to optimize?
- recognize repetition in the binary tree
- `gridTraveler(a,b)` has the same number of ways as `gridTraveler(b,a)`
- memoize !!!

```python
def gridTraveler(m,n,memo={}):
    key = str(m) + ',' str(n)
    if key in memo: return memo[key]
    if (m == 1 and n == 1) return 1
    if (m == 0 or n == 0) return 0
    memo[key] = gridTraveler(m-1,n,memo) + gridTraveler(m,n-1,memo)
    return memo[key]
```

For our new optimized solution:
- `m: {0, 1 ,2 ,3, 4}`
- `n: {0, 1, 2, 3}`
- m*n possible combinations

Brute force
- Time complexity: `O(2^{n+m})`
- Space complexity: `O(n+m)`

Memoized
- Time complexity: `O(m*n)`
- Space complexity: `O(n+m)`

NOTE: try to think about recursive calls as a tree

# canSum 
Write a function that takes in a targetSum and an array of numbers as arguments.

The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array.

You may use an element of the array as many times as needed
You may assume that all input numbers are nonnegative

example: 
- `canSum(7,[5,3,4,5])` -> true
- `canSum(7,[5,3,4,7])` -> true

```python
def canSum(targetSum,numbers):
    if (targerSum == 0): return True
    if (targetSum <0): return False
    for num in numbers:
        remainder = targetSum - num
        if (canSum(remainder,numbers)): return True
    return false
```

What is the max length or distance from the tree:
- you can subtract -1 at every level so the max height is m (target sum)
- the branching factor
    - if my array has 3 numbers, the node can have at most 3 children
- hence time complexity is `O(n^m)`
- we can memoize (certain subtree results can be cached into memo)

```python
def canSum(targetSum,numbers,memo={}):
    if targetSum in memo: return memo[targetSum]
    if (targerSum == 0): return True
    if (targetSum <0): return False
    for num in numbers:
        remainder = targetSum - num
        if (canSum(remainder,numbers,memo)): 
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return false
```
brute force
- `O(n^m)` time complexity
- `O(m)` space complexity
memoized
- `O(m*n)` time complexity
- `O(m)` space complexity


# howSum
Write a function that takes in a targetSum and an array of numbers as arguments

The function should return an array containingi any comhination of elements that add upt ot exactly the targetSum. If there is no combination that adds up to the targetSum, then return null

If there are multiple comninations possible, you may return any 
single one

1. 
`howSum(7,[5,3,4,7]) -> [7] or [3,4]`

2. 
`howSum(7,[2,4]) -> null`

3. 
`howSum(8,[2,3,5]) -> [2,2,2,2] or [3,5]`

4. 
`howSum(0,[1,2,3]) -> []`


```python
def howSum(targerSum,numbers):
    if (targetSum == 0) return []
    if (targetSum < 0) return null
    for num in numbers:
        remainder = targerSum - num
        result = howSum(remained,numbers)
        if result != null
            return [*result,num]
    return None
        
```
Time Complexity: `O((n^m)*m)`, n is length of array (branching factor), m is targetSum, but this line `[*result,num]` has additional time complexity. For each recursive call, you need to create a copy of the array.

Space Complexity: `O(m)`, worst case the array is length m


Memoized:
```python
def howSum(targerSum,numbers,memo):
    if targetSum in memo return memo[targetSum]
    if (targetSum == 0) return []
    if (targetSum < 0) return null
    for num in numbers:
        remainder = targerSum - num
        result = howSum(remained,numbers)
        if result != null
            memo[targetSum] = [*result,num] 
            return memo[targetSum]
    memo[targetSum] = None
    return None
        
```
Memoized time complexity: `O(n*m^2)` time
Memoized space complexity: `O(m^2)` space

# bestSum

Write a function that takes in a targetSum and an array of numbers as arguments. The function should return an array containing the shortest comnbination of numbers that add up to exactly the targetSum.

If there is a tie for the shortest combination, you may return any one of the shortest.

1. 
`bestSum(7,[5,3,4,7]) -> 7`

2.
`bestSum(8,[2,5,3) -> [5,3]`

```python

shortest = None

def bestSum(targerSum,numbers):
    if (targetSum == 0) return []
    if (targetSum < 0) return null
    for num in numbers:
        remainder = targerSum - num
        result = bestSum(remained,numbers)
        if result != null
            combo = [*result,num]
            if shortest is None or len(combo) < len(shortest):
                shortest = combo
    return None
        
```
- m is targetSum
- n is numbers length
Time Complexity: O(n*)