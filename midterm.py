def max_heapify(array,n,i):
    index = i
    left = 2*i
    right = 2*i+1
    largest = i
    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right
    
    if index != largest:
        array[i],array[largest] = array[largest],array[i]
        max_heapify(array,n,largest)

def build_max_heap(array):
    for i in range(len(array)//2,-1,-1):
        max_heapify(array,len(array),i)

def heapsort(array,n):
    #build the heap
    build_max_heap(array)
    # iterate through every node
    for i in range(n-1,0,-1):
        # at every iteration you extract the maximum element 
        array[i],array[0] = array[0],array[i]
        max_heapify(array,i,0)
    return array


def partition(array,low,high):
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] <= pivot:
            i += 1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[high] = array[high],array[i+1]
    return i+1

def quick_sort(array,low,high):
    if low < high:
        pi = partition(array,low,high)
        quick_sort(array,low,pi-1)
        quick_sort(array,pi+1,high)

if __name__ == "__main__":
    arr = [9, 4, 3, 8, 10, 2, 5] 
    heapsort(arr,len(arr))
    print("Heap Sort: Sorted array is ")
    print(arr)
    quick_sort(arr,0,len(arr)-1)
    print("Sorted array is ")
    print(arr)
