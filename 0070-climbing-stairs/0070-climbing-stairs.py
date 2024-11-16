class Solution:
    def climbStairs(self, n: int) -> int:
        if(n<=1):
            return 1
        p,c=1,1
        for i in range(2,n+1):
            p,c=c,p+c
        return c 