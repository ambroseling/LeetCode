import time
# Solution 1:
def mergeKSortedV1(arr):
    heap = []
    result = []
    for i in range(len(arr)): #O(k)
        heap.append(arr[i].pop(0)) #O(n/k)
    while notEmpty(arr): #O(k)
        build_heap(heap) # O(n lg n)
        result.append(heap.pop(0))  #O(k)
        smallest,index = extract_smallest(arr) # O(k)
        arr[index].pop(0) #O(n/k)
        heap.append(smallest)
    result.extend(heap)
    return result

def heapify(heap, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len(heap) and heap[left] < heap[smallest]:
        smallest = left
    if right < len(heap) and heap[right] < heap[smallest]:
        smallest = right
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        heapify(heap, smallest)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
def notEmpty(arr):
    for i in range(len(arr)):
        if len(arr[i]) > 0:
            return True
    return False

def build_heap(heap):
    for i in range(len(heap) // 2 - 1, -1, -1):
        heapify(heap, i)

def extract_smallest(arr):
    smallest = 10000000
    index = 0
    for i in range(len(arr)):
        if arr[i] and arr[i][0] < smallest:
            smallest = arr[i][0]
            index = i
    return smallest,index


# Cleaner solution 1:
import heapq

def mergeKSortedClean(arr):
    heap = []
    result = []
    # Initialize heap with the first element of each array along with the array index and element index
    for i in range(len(arr)):
        if arr[i]:
            heapq.heappush(heap, (arr[i][0], i, 0))
    
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        if element_idx + 1 < len(arr[list_idx]):
            next_tuple = (arr[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(heap, next_tuple)
    
    return result


# Solution 2:
# Function to merge K sorted lists using the merge sort approach
# Helper function to merge two sorted lists
def mergeTwoLists(list1, list2):
    merged = []
    i, j = 0, 0
    
    # Merge elements from both lists in sorted order
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append any remaining elements from both lists
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged
def mergeKSortedMerge(arr):
    if not arr:
        return []
    
    # Continue merging until we have only one list left
    while len(arr) > 1:
        merged_lists = []

        # Merge lists in pairs
        for i in range(0, len(arr), 2):
            if i + 1 < len(arr):
                merged_lists.append(mergeTwoLists(arr[i], arr[i + 1]))
            else:
                merged_lists.append(arr[i])  # If there's an odd number of lists, append the last one as is

        # Update arr to the newly merged lists
        arr = merged_lists

    return arr[0]  # The final merged list



if __name__ == "__main__":
    arr = [
        [23,59,89,123,234,788],
        [10,22,24,45,67,98],
        [30,31,32,56,90,121]
    ]
    start1 = time.monotonic()
    result1 = mergeKSortedClean(arr)
    stop1 = time.monotonic()
    print(f"Diff 1: {stop1 - start1} in s")
    print(result1)
    arr = [
        [23,59,89,123,234,788],
        [10,22,24,45,67,98],
        [30,31,32,56,90,121]
    ]
    start2 = time.monotonic()
    result2 = mergeKSortedV1(arr)
    stop2 = time.monotonic()
    print(f"Diff 2: {stop2 - start2} in s")
    print(result2)

