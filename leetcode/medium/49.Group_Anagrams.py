import collections

class Solution(object):
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = collections.defaultdict(list)    # Make empty dictionary(list type)
        
        for word in strs:
            anagrams["".join(sorted(word))].append(word)
        
        return list(anagrams.values())


# class Solution(object):
#     def groupAnagrams(self, strs):
        
#         sorted_strs = ["".join(sorted(word)) for word in strs]
#         anagrams = {}
#         for str in sorted_strs:
#             if str not in anagrams:
#                 anagrams[str] = []
        
#         for str in strs:
#             if "".join(sorted(str)) in anagrams:
#                 anagrams["".join(sorted(str))].append(str)
        
#         return list(anagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]

solution = Solution()
solution.groupAnagrams(strs)