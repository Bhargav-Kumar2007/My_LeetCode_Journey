class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int []ret=new int[2];
        ret[0]=0;ret[1]=numbers.length-1;
        while(ret[0]<ret[1]){
            if(numbers[ret[0]]+numbers[ret[1]]<target)ret[0]+=1;
            else if(numbers[ret[0]]+numbers[ret[1]]>target)ret[1]-=1;
            else break;
        }
        ret[0]+=1;
        ret[1]+=1;
        return ret;
    }
}