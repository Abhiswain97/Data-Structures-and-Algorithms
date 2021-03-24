# Needs fixing !!


import sys
import math
from pprint import pprint

def mcm(arr):

    n = len(arr)
    dp = [[0 for _ in range(n)]  for _ in range(n)]
    
    for i in range(1, n):
        dp[i][i] = 0

    for d in range(1, n):
        for i in range(1, n-d):
            j = i + d

            m = sys.maxsize

            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + (arr[i-1] * arr[k] * arr[k])
                if q < m:
                    m = q

            dp[i][j] = m
        
        pprint(dp)
            
    return dp[1][n-1] 

if __name__ == '__main__':

    arr = [5, 4, 6, 2, 7]

    print(mcm(arr))