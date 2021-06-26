class Solution(object):
    def longestPalindrome(self, s: 'str') -> 'str':
        """
        :type s: str
        :rtype: str
        """
        # 팰린드롬 판별 및 투 포인터 확장. 
        def expand(left: 'int', right: 'int') -> 'str':
            """
            :type left: int
            :type right: int
            :rtype: str
            """
            while left >= 0 and right <len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        # 주어진 문자열 자체가 팰린드롬이면 바로 리턴. 
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        # 슬라이딩 윈도우 오른쪽으로 이동. 
        for i in range(len(s) - 1):
            result = max(result,
                            expand(i, i + 1),
                            expand(i, i + 2),
                            key=len)
        return result

# solution = Solution()
# s = "123454321"
# print(solution.longestPalindrome(s))