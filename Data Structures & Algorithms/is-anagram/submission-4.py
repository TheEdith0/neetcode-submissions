class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=sorted(s)
        l2=sorted(t)
        if(len(l1)!=len(l2)):
            return False
        for i in range(0,len(l1)):
            if(l1[i]!=l2[i]):
                return False
        return True
        