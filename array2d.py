#!/usr/bin/python3
H=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,33,12],
    [13,14,15,16]
    ]



def hourglass(a,i,j): # The hourglass function
    
    sum = int(0)
    
    for p in a[i-1][j-1],a[i-1][j],a[i-1][j+1],a[i][j],a[i+1][j-1],a[i+1][j],a[i+1][j+1]:  # iterating over the hourglass 
        sum += p

    return sum


s = [] # Empty single dimensional list

for i in range(1,3):
    for j in range(1,3):
        d = hourglass(H,i,j)
     
        s.append(int(d))



#Bubble sorting the array with sum of hourglasses in descending order 
n = len(s)
for i in range(n):
    for j in range(n-i-1):
        if s[j] < s[j+1]:
            s[j],s[j+1] = s[j+1],s[j]

#Printing the maximum of sum
print(s[0])
        

