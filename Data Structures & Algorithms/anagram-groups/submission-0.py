class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs2=[]
        for i in range(len(strs)):
            strs2.append(''.join(sorted(strs[i])))
        hash_strs={}
        for i in range(len(strs2)):
            if(strs2[i] in hash_strs):
                hash_strs[strs2[i]].append(strs[i])
            else:
                hash_strs[strs2[i]]=[strs[i]]
        strs2=[]
        for i in hash_strs:
            strs2.append(hash_strs[i])
        return strs2
               




