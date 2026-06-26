class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        final = ""
        for i in words:
            lol=0
            for j in i:
                lol+=weights[(ord(j) - 97)]
            final+="zyxwvutsrqponmlkjihgfedcba"[lol%26]
        return final