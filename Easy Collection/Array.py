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
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        if l!=1:
            nums[:]=nums[l-k:]+nums[:l-k]
            
###Contains Duplicate###
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=len(nums)
        if l>len(set(nums)):
            return(True)
        else:
            return(False)
        
###Single Number###
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(set(nums)))*2-sum(nums)
"""
可以用xor  a^a=0, a^b!=0
"""

###Intersection of Two Arrays II###    
    class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        a=0
        b=0
        res=[]
        while a<len(nums1) and b<len(nums2):
            if nums1[a]==nums2[b]:
                res.append(nums1[a])
                a+=1
                b+=1
            elif nums1[a]<nums2[b]:
                a+=1
            else:
                b+=1
        return res

###Plus One###
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum=0
        res=[]
        for i in range(len(digits)):
            sum+=digits[len(digits)-1-i]*(10**i)
        sum+=1
        for i in range(len(str(sum))):
            res.append(int(str(sum)[i]))
        return res

###Move Zeroes###
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        res=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                res.append(nums[i])
        diff=len(nums)-len(res)
        for i in range(diff):
            res.append(0)
        nums[:]=res
        
###Two Sum###
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    res.append(i)
                    res.append(j)
                    break
        return res
    """
    用dic和enumerate
    """
    
    ###Valid Sudoku###
    class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen=[]
        for i,row in enumerate(board):
            for j,val in enumerate(row):
                if val!=".":
                    seen+=[(val,j),(i,val),(i/3,j/3,val)]
        return len(seen)==len(set(seen))

###Rotate Image###
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:]=zip(*matrix[::-1])
"""
A[::-1]翻转A
zip(*A)=zip(A[0],A[1],...) 转置A
[list(i) for i in zip(*A)] 
"""
