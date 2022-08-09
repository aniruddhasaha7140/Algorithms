class Solution:
    def partitionLabels(self, s: str):
        d={}
        l=end=start=0
        output=[]
        for index in range(0,len(s)):
            d[s[index]]=index
        for ch in s:
            l+=1
            if d[ch] > end:
                end=d[ch]
            if start==end:
                output.append(l)
                l=0
            start+=1
        return output
    
s=Solution()
out=s.partitionLabels("ababcbacadefegdehijhklij")
print(s.partitionLabels("eccbbbbdec"))
print(out)

class Solution1(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans
