class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPal = ""
        for i in range(len(s)):
            # Impaire
            leftIndex = i - 1
            rightIndex = i + 1
            while leftIndex >= 0 and rightIndex < len(s) and s[leftIndex] == s[rightIndex]:
                leftIndex -= 1
                rightIndex += 1

            currentPal = s[leftIndex + 1:rightIndex]
            maxPal = max(maxPal, currentPal, key=len)

            # Pair
            leftIndex = i
            rightIndex = i + 1
            while leftIndex >= 0 and rightIndex < len(s) and s[leftIndex] == s[rightIndex]:
                leftIndex -= 1
                rightIndex += 1

            currentPal = s[leftIndex + 1:rightIndex]
            maxPal = max(maxPal, currentPal, key=len)

        return maxPal


    




