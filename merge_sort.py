def merge(arr,left,mid,right):
    l = arr[left:mid+1]
    r = arr[mid+1:right+1]
    i = 0
    j = 0
    k = left
    while i < len(l) and j < len(r):
        if l[i] <= r[j] :
            arr[k] = l[i]
            i+=1
        else:
            arr[k] = r[j]
            j+=1
        k+=1
    while i < len(l):
        arr[k] = l[i]
        i+=1
        k+=1

    while j < len(r):
        arr[k] = r[j]
        j+=1
        k+=1


def merge_sort(arr,left,right):
    if left < right:
        mid = (left + right) //2 
        merge_sort(arr,left,mid)
        merge_sort(arr,mid+1,right)
        merge(arr,left,mid,right)
    

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    merge_sort(arr,0,len(arr)-1)
    print(arr)