class Solution(object):
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        """
        일반적인 브루트 포스로 풀면 시간복잡도가 O(n^3)으로 시간 초과가 발생한다.
        투 포인터를 활용하여 O(n^2)안에 푸는 방법을 이용.
        """
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:    # 중복값이면 건너뛴다. 
                continue
            
            left, right = i + 1, len(nums) - 1      # 투 포인터 설정.
            while left < right:                     # 좁혀가며 합을 계산.
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] ==  nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

        return result
        
# solution = Solution()
# nums = [-1, 0, 1, 2, -1, -4]
# print(solution.threeSum(nums))
