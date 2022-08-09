class Solution:
    def countSubstrings(self, s: str) -> int:   
        def palin(sub):
            if sub==sub[::-1]:
                return True
            return False
        res=[]
        substring=[]
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                substring=s[i:j]
                if palin(substring)==True:
                    res.append(substring)
        return len(res)

class Solution:
    def countSubstrings(self, s: str) -> int:   
        res=0
        for i in range(len(s)):
            l=r=i
            while l >= 0 and r < len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            l=i
            r=i+1
            while l >= 0 and r < len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
        return res            
