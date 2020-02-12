#Here we have to fill a brick of dimension 1*4 into a n*4 dimension
# the problem stated can be approached in two ways one is Recursion based and the other is using
#using Dynamic programming as it has overlapping sub-problems and recursion
#Timeand space complexity for Dynamic programming O(n)


#recursion based approach
def fillbrick(n):
    if n==0 or n==1 or n==2 or n==3:
        return 1 
    return fillbrick(n-1)+fillbrick(n-4)
if __name__ == '__main__':
    print(fillbrick(4))
    
#based on Dynamic programming
def fillbrick_dp(n):
    dp=[0]*(n+1)
    dp[0],dp[1],dp[2],dp[3]=1,1,1,1
    for i in range(4,n+1):
        dp[i]=dp[i-1]+dp[i-4]
    return dp[n]
if __name__ == '__main__':
    print(fillbrick_dp(8))