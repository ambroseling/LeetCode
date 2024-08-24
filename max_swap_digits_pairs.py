def solution(numbers):
    numbers = sorted(numbers)
    for i,num in enumerate(numbers):
        if i < len(numbers)-1:
            next_num = numbers[i+1]
        while len(str(next_num)) <= len(str(num)):
            nums = list(num)
            next_num = list(next_num)
            d = []
            # 
            for i in range(len(nums)):
                if nums[i] != next_num[i]:
                    d.append(i)




        


if  __name__ == "__main__":
    numbers = [1,23,156,1650,651,165,32]
    occ = solution(numbers)
    print(occ)
