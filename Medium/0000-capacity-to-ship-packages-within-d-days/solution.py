class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int left = 0;
        int right = 0;
        for (int w : weights) {
            left = Math.max(left, w);
            right += w;    
        }
        
        int result = right;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (canShip(weights, days, mid)) {
                result = mid;       
                right = mid - 1;     
            } else {
                left = mid + 1;      
            }
