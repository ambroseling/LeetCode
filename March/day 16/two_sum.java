import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> diff = new HashMap<>(nums.length);

        for (int i = 0; i < nums.length; i++){
            int complement = target-nums[i];
            if (diff.containsKey(complement )){
                return new int[] {diff.get(complement ), i};
            }
            diff.put(nums[i],i);
        }
        
        return null;
    }
   
}