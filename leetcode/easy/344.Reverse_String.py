class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
    
        return s.reverse()



solution = Solution()
s = ["a", "s", "f", "l"]
print(solution.isPalindrome(s))

