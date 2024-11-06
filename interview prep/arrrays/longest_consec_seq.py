class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet: #if there is no left neighbor, then it is the start of a sequence
            # so for each starting element, 
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest




    # turn into a set
    # go htrough each elemetn 
    # is it a starting point value so if there nis no left neigbour 
    # then we know that this is the start of a sequence
    # we use a while loop to count the length of the sequence, wheever there is not a next consecutive number, we stop iterating 
    # we update the longest sequence length if the current sequence is longer


    