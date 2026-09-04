class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        in_segment = False
        
        for char in s:
            if char != ' ' and not in_segment:
                count += 1
                in_segment = True
            elif char == ' ':
                in_segment = False
        
        return count