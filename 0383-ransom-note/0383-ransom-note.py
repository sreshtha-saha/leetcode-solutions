class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = [0] * 26
        
        for char in magazine:
            counts[ord(char) - ord('a')] += 1
        
        for char in ransomNote:
            index = ord(char) - ord('a')
            counts[index] -= 1
            if counts[index] < 0:
                return False
        
        return True