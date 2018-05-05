###Remove Duplicates from Sorted Array###
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        else:
            cur=0
            for i in range(1,len(nums)):
                if nums[cur]!=nums[i]:
                    nums[cur+1]=nums[i]
                    cur+=1 
        return cur+1
       
       
       
###Best Time to Buy and Sell Stock II###
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        if len(prices)<2:
            return profit
        else:
            for i in range(1,len(prices)):
                if prices[i-1]<prices[i]:
                    profit+=(prices[i]-prices[i-1])
        return profit
        
        
       
###Rotate Array###