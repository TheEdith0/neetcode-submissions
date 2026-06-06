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
            if(t[i] in d):
                d[t[i]]+=1
            else:
                d[t[i]]=1
        for key,value in d.items():
            if((value%2)!=0):
                return False
            if(key not in s or key not in t):
                return False
            
        return True

                            
    