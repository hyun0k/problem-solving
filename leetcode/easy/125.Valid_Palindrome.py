import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()                     # Convert s to lower case.
        s = re.sub('[^a-z0-9]', '', s)    # Remove character except for alphanumeric.

        return s == s[::-1]



solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))

