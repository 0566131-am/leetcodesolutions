class Solution {
    public int maxSubArray(int[] nums) {
        for(int i=1;i<nums.length;i++){
           currentSum=Math.max(nums[i],currentSum+nums[i]);
        }
        return maxsum;
        
    }
        int currentSum=nums[0];
        int maxsum=nums[0];

           maxsum=Math.max(maxsum,currentSum);
}
