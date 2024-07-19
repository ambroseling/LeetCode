class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(arr,low,high):
            pivot = arr[high]
            i = low - 1 # i is kind of keeping track of the wall, or seperatino boundary btw the 2 partitions

            for j in range(low,high):
                if arr[j] > pivot:
                    i += 1
                    (arr[j],arr[i]) = (arr[i],arr[j])
            (arr[high],arr[i+1]) = (arr[i+1],arr[high])
            return i+1
        
        def quickselect(arr,k,low,high):
            p = partition(arr,low,high)
            #if k is smaller than p
            if k < p:
                if len(set(arr[low:p])) > 1:
                    return quickselect(arr,k,low,p-1)
                else:
                    return arr[k]
            elif k > p:
                if len(set(arr[p+1:high+1])) > 1:
                    return quickselect(arr,k,p+1,high)
                else:
                    return arr[k]
            else:
                return arr[p]

        val = quickselect(nums,k-1,0,len(nums)-1)
        return val
    
    
if __name__ == "__main__":
    s = Solution()
    nums = [10,80,30,90,40,50,70]
    k = 4
    import ipdb; ipdb.set_trace()
    s.findKthLargest(nums,k-1)