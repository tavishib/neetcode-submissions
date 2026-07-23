class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        s = s.lower()
        while right > left:
            while not s[right].isalnum() and right > 0:
                right -= 1
            while not s[left].isalnum() and left < len(s)-1:
                left += 1
            if s[right] != s[left] and right != 0 and left != len(s)-1:
                return False
            right -= 1
            left += 1
        return True