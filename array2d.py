#!/usr/bin/python3
H = []
for _ in range(6):
        H.append(list(map(int, input().rstrip().split())))


#print(H)
'''H=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,33,12],
    [13,14,15,16]
    ]'''



def hourglassSum(a): # The hourglass function
    
    sum = int(0)
    sum_arr = []

    for i in range(1,5):
        for j in range(1,5):
            for p in a[i-1][j-1],a[i-1][j],a[i-1][j+1],a[i][j],a[i+1][j-1],a[i+1][j],a[i+1][j+1]:
                sum += p  # iterating over the hourglass 
                sum_arr.append(sum)
                sum = 0 

    
    n = len(sum_arr)
    for i in range(n): 
        for j in range(n-i-1):
            if sum_arr[j] < sum_arr[j+1]:
                sum_arr[j],sum_arr[j+1] = sum_arr[j+1],sum_arr[j]


    return sum_arr[0]
    
g = hourglassSum(H)
print(g)

        

