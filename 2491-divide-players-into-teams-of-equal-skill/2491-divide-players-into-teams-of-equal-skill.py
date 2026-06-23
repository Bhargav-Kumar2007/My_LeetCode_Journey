class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        x=len(skill)
        m=sum(skill)*2/x
        nl=0
        for i in range(x//2):
            if skill[0]+skill[-1]!=m:
                return -1
            nl+=skill.pop(0)*skill.pop(-1)
        return nl