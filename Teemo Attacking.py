class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res=0
        if not timeSeries:
            return res
        else:
            res+=duration
        for i in range(1,len(timeSeries)):
            if timeSeries[i]-timeSeries[i-1]<duration:
                res+=timeSeries[i]-timeSeries[i-1]
            else:
                res+=duration
        return res
                
