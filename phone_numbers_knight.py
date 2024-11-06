def knight_moves(digits):
    A = [
        [4,6],
        [8,6],
        [7,9],
        [4,8],
        [3,9,0],
        [],
        [1,7,0],
        [2,6],
        [1,3],
        [2,4]
    ]
    prev_nums = [0] * 10
    curr_nums = [0] * 10

    for k in range(1, digits + 1):
        # A[i] = number of moves from i
        for i in range(10):
            if k == 1:
                curr_nums[i] = 1
            else:
                # if i is 0, then  can only go to 4 or 6
                for j in A[i]:
                    curr_nums[i] += prev_nums[j]
        prev_nums = curr_nums
        curr_nums = [0] * 10

    return sum(prev_nums)


print("Number of possible phone numbers with 1 digit:", knight_moves(1))
print("Number of possible phone numbers with 2 digits:", knight_moves(2))
print("Number of possible phone numbers with 3 digits:", knight_moves(3))



# def knight_moves(digits):
#     A = [
#         [4,6],
#         [8,6],
#         [7,9],
#         [4,8],
#         [3,9,0],
#         [],
#         [1,7,0],
#         [2,6],
#         [1,3],
#         [2,4]
#     ]
#     prev_nums = [0] * 10
#     curr_nums = [0] * 10
#     if digits == 1:
#         return len(A)
#     for n in range(2, digits+1):
#         # A[i] = number of moves from i
#         for i in range(10):
#             if n == 2:
#                 prev_nums[i] = len(A[i])
#             else:
#                 # if i is 0, then  can only go to 4 or 6
#                 for j in A[i]:
#                     curr_nums[i] += prev_nums[j]    
#     if n == 2:
#         curr_nums = prev_nums
#     return sum(curr_nums)


# if __name__ == "__main__":
#      print("Number of possible phone numbers with 1 digit:", knight_moves(1))
#      print("Number of possible phone numbers with 2 digits:", knight_moves(2))
#      print("Number of possible phone numbers with 3 digits:", knight_moves(3))

