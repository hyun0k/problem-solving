class Solution(object):
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        """
        target에서 nums의 수를 뺀 값을 nums_map에서 찾는 방법.
        nums_map은 nums의 각 수를 키값으로 가지고 index를 값으로 가지는 자료구조.
        """
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [i, nums_map[target - num]]
            nums_map[num] = i

# solution = Solution()
# nums = [2,7,6,10]
# target = 9
# print(solution.twoSum(nums, target))
