class Solution {
    public int maxSubArray(int[] nums) {
        int cursum = nums[0];
        int bsum= nums[0];
        
        for (int i=1; i <nums.length;i++){
            cursum=Math.max(nums[i],cursum+nums[i]);
            bsum=Math.max(bsum,cursum);
        }
        return bsum;
    }
}