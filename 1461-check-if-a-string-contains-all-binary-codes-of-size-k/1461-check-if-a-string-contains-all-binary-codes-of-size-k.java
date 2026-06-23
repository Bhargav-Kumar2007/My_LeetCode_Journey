class Solution {
    public boolean hasAllCodes(String s, int k) {
        if(s.length()<k){
            return false;
        }
        int target=1<<k;
        boolean[] seen = new boolean[target];
        int c=0;
        int num=Integer.parseInt(s.substring(0,k),2);
        seen[num]=true;
        c++;
        for(int i=k;i<s.length();i++){
            int mask = (1 << k) - 1;
            num = ((num << 1) & mask) | (s.charAt(i) - '0');
            if(seen[num]==false){
                seen[num]=true;
                c++;
            }
            if(c==target)return true;
        }
        return false;
    }
}