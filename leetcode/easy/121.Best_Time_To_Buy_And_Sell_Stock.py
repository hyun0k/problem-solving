import sys

class Solution(object):
    def maxProfit(self, prices: 'List[int]') -> int:
        """[summary]
        브루트 포스로 풀면 O(n^2)에 풀 수 있긴 하지만 시간 초과가 발생한다.
        최저점을 갱신하면서 현재 값과의 차이를 계산하는 방법으로 O(n)에 풀이.
        """
        min_price = sys.maxsize
        max_profit = -sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

        # 브루트 포스
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, profit)

        # return max_profit


# solution = Solution()
# prices = [7,1,5,3,6,4]
# print(solution.maxProfit(prices))

