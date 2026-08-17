class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings)==1:
            return 1
        if len(ratings)==0:
            return 0
        lst=[1 for _ in ratings]
        count=len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1] and lst[i]<=lst[i-1]:
                count+=lst[i-1]-lst[i]+1
                lst[i]=lst[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1] and lst[i]<=lst[i+1]:
                count+=lst[i+1]-lst[i]+1
                lst[i]=lst[i+1]+1
        return count
                