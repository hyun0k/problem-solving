class Solution(object):
    def arrayPairSum(self, nums: 'List[int]') -> 'int':
        """
        정렬해서 0번째 인덱스부터 짝수번째 인덱스에 해당하는 수의 합을 구한다.
        """
        return sum(sorted(nums)[::2])

# solution = Solution()
# nums = [1,4,3,2]
# print(solution.arrayPairSum(nums))

        