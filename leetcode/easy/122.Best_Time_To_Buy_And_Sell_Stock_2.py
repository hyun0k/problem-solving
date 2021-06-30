class Solution(object):
    def maxProfit(self, prices: 'List[int]') -> 'int':
        """[summary]
        여러 번 사고 팔 수 있으므로 산 시점 이후에 오르기만 하면 무조건 팔고 이를 계속 반복한다.
        """

        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
        
        # profit = 0
        # for i in range(len(prices) - 1):
        #     if prices[i + 1] > prices[i]:
        #         profit += prices[i + 1] - prices[i]
            
        # return profit

# solution = Solution()
# prices = [7,1,5,3,6,4]
# print(solution.maxProfit(prices))
        