import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip = s.replace(" ", "").lower()
        strip = re.sub(r"[^a-zA-Z0-9]", "", strip)
        for x in range(int(len(strip)/2)):
            if strip[x] != strip[len(strip) - x - 1]:
                return False
        return True
