def solution(arr):
    left = 0
    right = len(arr)-1
    volume = (right - left) * (arr [right] if arr[right] < arr[left] else arr[left])
    import ipdb; ipdb.set_trace()
    while left < right:
        if right-1 >0 and (right - 1 - left) * (arr [left] if arr[left] < arr[right-1] else arr[right-1]) > volume:
            right -=1
            volume = (right - left) * ( arr [right] if arr[right] < arr[left] else arr[left] )

        elif left + 1 < len(arr)-1 and (right - (left + 1) ) * (arr [right] if arr[right] < arr[left+1] else arr[left+1]) > volume:
            left +=1
            volume = (right - left) * ( arr [right] if arr[right] < arr[left] else arr[left] )
        else:
            return volume

    return volume



if __name__ == "__main__":
    height = [1,2,1]
    output = solution(height)
    print(output)
    # 11 ms