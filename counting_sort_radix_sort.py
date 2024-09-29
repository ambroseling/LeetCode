def countingSort(arr,exp):
    n = len(arr)
    # this is the output array
    output = [0] * n
    # this array keeps track of the counts for each number 0-9
    count  = [0] * 10
    # import ipdb; ipdb.set_trace(context=5)
    # go through all the elements in your array
    for i in range(0,n):
        # array element divided by i.e. 123 // 1 = 123 
        index = arr[i] // exp
        # then get the last digit of this number 3, and add a 1 to that number in count
        count[index % 10] += 1
    # import ipdb; ipdb.set_trace(context=5)
    # [2, 0, 2, 0, 1, 2, 1, 0, 0, 0]
    # do a prefix sum on the counts of all single digit numbers
    for i in range(1,10):
        count[i] += count[i-1]
    # import ipdb; ipdb.set_trace(context=5)
    # [2, 2, 4, 4, 5, 7, 8, 8, 8, 8]
    # after 66 is put into output, we subtract the occurence for that i
    # [2, 2, 4, 4, 5, 7, 7, 8, 8, 8]
    # count[i]  represents the number of occurences for digits <= i
    i = n-1
    # start from the end of the array
    while i >= 0:
        index = arr[i] // exp
        # count[digit of interest] 
        # i guess count basically tells you how many numbers come before i
        # so count[3] = 4 means there are 4 numbers (or occurences of numbers) that came before digit 3
        # if you know that 4 numbers come before it then this tells you where should this number go in the output array
        output[count[index%10] - 1] = arr[i]
        # subtract the number of occurences 
        count[index%10] -= 1
        i  -= 1
    
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    largest = max(arr)
    exp = 1
    while  largest / exp >= 1:
        countingSort(arr,exp)
        exp *= 10
    


if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    # import ipdb; ipdb.set_trace(context=5)
    radixSort(arr)
    print(arr)