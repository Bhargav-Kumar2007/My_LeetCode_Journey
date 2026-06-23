class Solution {
    public int maxArea(int[] height) {
        int ma=0,low=0, high=height.length-1;
        while(low<high){
            int x;
            if(height[low]<height[high]) x = height[low]; 
            else x = height[high];
            if((high-low)*x>ma){
                ma=(high-low)*x;
            }
            if(height[low]>=height[high]){
                high-=1;
            }
            else if(height[low]<height[high]){
                low+=1;
            }
        }
        return ma;
    }
}