class Solution {
    public void sortColors(int[] nums) {
        int r=0,w=0,b=0;
        for (int i:nums){
            if(i==0){
                r++;w++;b++;
            }
            else if(i==1){
                w++;b++;
            }
            else if(i==2){
                b++;
            }
        }
        for (int i = 0; i < r; i++) {
            nums[i] = 0;
        }
        for (int i = r; i < w; i++) {
            nums[i] = 1;
        }
        for (int i = w; i < b; i++) {
            nums[i] = 2;
        }
    }
}