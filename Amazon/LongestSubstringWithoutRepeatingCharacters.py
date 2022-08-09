class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup=set()
        substr=[]
        long=0
        l=0
        r=1
        for ch in s:
            if ch in dup:
                dup.remove(ch)
                l+=1
            dup.add(ch)
            substr=s[l:r]
            long=len(substr)
            r+=1
                
        return long

s=Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup=set()
        long=0
        l=0
        for r in range(0,len(s)):
            while s[r] in dup:
                dup.remove(s[l])
                l+=1
            dup.add(s[r])
            long=max(long,r-l+1)
                
        return long