class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        if (len(s)!=len(t)):
            return False
        for i in range(0,len(s)):
            if(s[i] in d):
                d[s[i]]+=1
            else:
                d[s[i]]=1
        for i in range(0,len(t)):
            if(t[i] in d):
                d[t[i]]+=1
            else:
                return False

        for value in d.values():
            if(value%2 != 0):
                return False
        return True

                            
    