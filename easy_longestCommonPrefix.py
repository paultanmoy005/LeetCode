class Solution:
    def longestCommonPrefix(self, strs):
        eachLen = [len(i) for i in strs]
        minLen = eachLen.index(min(eachLen))
        if strs[minLen]=="":
            return ""
        else:
            idx = 0
            pref = strs[minLen][idx]
            prefAll = [strs[i][idx] for i in range(len(strs))]
            while len(set(pref).union(set(prefAll))) == 1 and pref in prefAll and idx < len(strs[minLen]):
                idx = idx+1
                if idx < len(strs[minLen]):
                    pref = strs[minLen][idx]
                    prefAll = [strs[i][idx] for i in range(len(strs))]
            if idx == 0:
                return ""
            else:
                return strs[minLen][:idx]
