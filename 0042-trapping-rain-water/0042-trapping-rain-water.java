class Solution {
    public int trap(int[] height) {
        int lvl=0,total=0,tmns=0,low=0,high=height.length-1,lst=0;
        if(height.length<=2) return 0;
        while(low<high){
            int less;
            if (height[low]<height[high])less=height[low];
            else less=height[high];
            if(lvl<less){
                total+=(less-lvl)*(high-low-1);
                lvl=less;
            }
            if(height[low]>=height[high]){
                high-=1;
                if(height[high]>=lvl)tmns+=lvl;
                else tmns+=height[high];

            }
            else if(height[low]<height[high]){
                low+=1;
                if(height[low]>=lvl)tmns+=lvl;
                else tmns+=height[low];
            }
        }
        return total-tmns+lvl;

    }
}