class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
    
        left = 0
        max_length = 0
        charDict = {}
    
        for right in range(len(s)):
            if s[right] in charDict and charDict[s[right]] >= left:
                left = charDict[s[right]] + 1
    
            charDict[s[right]] = right
            max_length = max(max_length, right - left + 1)
    
        return max_length
            

s = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))