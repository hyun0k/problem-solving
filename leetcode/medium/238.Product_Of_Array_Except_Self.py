class Solution(object):
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        """[summary]
        나눗셈없이 O(n)안에 풀어야 하므로 이중 for문은 사용할 수 없다.
        자신의 왼쪽에 있는 수를 모두 곱한 결과와 오른쪽에 있는 수를 모두 곱한 결과를 서로 곱하면 된다.
        양 끝에 있는 수의 옆에는 1이 있다고 생각하고 곱한다.
        """
        result = []
        p = 1
        for i in range(len(nums)): # 왼쪽 곱셈
            result.append(p)
            p = p * nums[i]
        
        p = 1
        for i in range(len(nums) - 1, -1, -1):  # 왼쪽 곱셈 결과에 오른쪽 곱셈
            result[i] = result[i] * p
            p = p * nums[i]
        
        return result

# solution = Solution()
# nums = [1,2,3,4]
# print(solution.productExceptSelf(nums))
        