class Solution:
    def isPalindrome(self, s: str) -> bool:
         s = s.lower()
         l = 0
         r = len(s)-1
         while l < r:
            #if ord(s[l]) < 97 or ord(s[l]) > 122:
            if not s[l].isalnum():
                l = l + 1
                continue
            #if ord(s[r]) < 97 or ord(s[r]) > 122:
            if not s[r].isalnum():
                r = r - 1
                continue
            if s[l] != s[r]:
                return False
            l = l + 1
            r = r - 1
         return True