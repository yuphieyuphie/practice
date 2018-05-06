###Reverse String###
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        
###Reverse Integer###
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            res=-int(str(-x)[::-1])
        else:
            res=int(str(x)[::-1])
        if ((res<-2**31) or (res>2**31-1)):
            return 0
        else:
            return res
        
###First Unique Character in a String###
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l)==1]
        return min(index) if len(index)>0 else -1
    
###Submission Detail###
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s)==sorted(t)

###Valid Palindrome###
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list=[]
        ns=''.join(x for x in s.lower() if x.isalpha() or x.isdigit())
        l=len(ns)
        for i in range(int(l/2)):
            if ns[i]!=ns[l-1-i]:
                list.append(i)
        return len(list)==0
"""
后面一坨可以改成
s==s[::-1]
"""
