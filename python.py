import os
import sys
import math

print('hello')

# nums = [1,4,2,4]
# maxes = [5,8]

# finalarray = [] 
# arrcnt = 0
# for maxe in maxes:
#     for num in nums:
#         if num < maxe:
#             arrcnt +=1
#     finalarray.append(arrcnt)
#     arrcnt = 0



# # Sock Merchant problem. return number of matched pairs

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9
# dict = {'a': 100, 'b':200, 'c':300}
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dictionaryCounter = {}

    for i in ar:
        if i in dictionaryCounter.keys():
            dictionaryCounter[i] += 1
        else:
            dictionaryCounter[i] = 1

    print(dictionaryCounter)

    matchCounter = 0

    for i in dictionaryCounter.values():
        matchCounter += math.trunc(i/2)

    return matchCounter

if __name__ == '__main__':
    print(sockMerchant(n,ar))

