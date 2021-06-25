import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = re.sub('[^\w]', ' ', paragraph).lower().split()
        words_not_banned = [word for word in words if word not in banned]

        words_count = {}
        for word in words_not_banned:
            if word not in words_count:
                words_count[word] = 0            
            words_count[word] += 1
        
        return max(words_count, key=words_count.get)

solution = Solution()
p = "Bob hit a ball, the hit BALL flew far after it was hit."
b = ["hit"]
print(solution.mostCommonWord(p, b))