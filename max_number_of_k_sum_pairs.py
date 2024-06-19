
#how to make this faster?
def solution(arr,k):
    left = 0
    right = left + 1
    ops = 0
    while right <= len(arr)-1 and left< len(arr)-1:
        if arr[right]+arr[left] == k:
            arr.pop(left)
            arr.pop(right-1)
            ops +=1
            left = 0
            right = left+1
        else:

            if right+1 > len(arr)-1:
                left+=1
                right = left+1
            else:
                right+=1

    return ops

if __name__ == "__main__":
    nums= [3,1,3,4,3]
    k = 6
    output = solution(nums,k)
    print(output)
    # 16 ms


# [1,2,3,4]
# {
# 1:4
# 
# }

# each pair you need to iterate at least through 