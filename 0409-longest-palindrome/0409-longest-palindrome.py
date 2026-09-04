class Solution:
    def longestPalindrome(self, s: str) -> int:
        unmatched = set()
        
        for char in s:
            if char in unmatched:
                unmatched.remove(char)
            else:
                unmatched.add(char)
        
        return len(s) - len(unmatched) + (1 if unmatched else 0)