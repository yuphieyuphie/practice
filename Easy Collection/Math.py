###Fizz Buzz###
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l=[]
        for i in range(n):
            if (i+1) % 15==0:
                l.append("FizzBuzz")
            elif (i+1) % 5==0:
                l.append("Buzz")
            elif (i+1) % 3==0:
                l.append("Fizz")
            else:
                l.append(str(i+1))
        return l

###Count Primes###
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isprime=[True]*max(2,n)
        isprime[0],isprime[1]=False,False
        x=2
        while x*x<n:
            if isprime[x]:
                p=x*x
                while p<n:
                    isprime[p]=False
                    p+=x
            x+=1
        return sum(isprime)
    
###Power of Three###
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        while n>1:
            if n%3==0:
                n/=3
                continue
            else:
                return False
        return True
    
###Roman to Integer###
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}   
        res=0
        while s:
            if s[:2] in d:
                res+=d[s[:2]]
                s=s[2:]
            else:
                res+=d[s[:1]]
                s=s[1:]
        return res
