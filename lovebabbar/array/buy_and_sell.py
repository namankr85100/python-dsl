class Solution(object):
   def maxProfit(self, prices):
      """
      :type prices: List[int]
      :rtype: int
      """
      ans = 0
      for i in range(1,len(prices)):
         if prices[i] - prices[i-1] >0:
            ans+=(prices[i] - prices[i-1])
      return ans
ob1 = Solution()
print(ob1.maxProfit([7,2,5,8,6,3,1,4,5,4,7]))
# Input
# print(ob1.maxProfit([7,2,5,8,6,3,1,4,5,4,7]))
# Output
# 13