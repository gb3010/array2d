#!/usr/bin/python3
H=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
#i=1;j=1
Z=[]
#print(a[i-1][j-1],a[i-1][j],a[i-1][j+1]) ; print(" ",a[i][j]);print(a[i+1][j-1],a[i+1][j],a[i+1][j+1])

def hourglass(a,i,j):
    
    sum = int(0)
    #print( a[i-1][j-1],a[i-1][j],a[i-1][j+1]) ; print(" ",a[i][j]);print(a[i+1][j-1],a[i+1][j],a[i+1][j+1] )
    for p in a[i-1][j-1],a[i-1][j],a[i-1][j+1],a[i][j],a[i+1][j-1],a[i+1][j],a[i+1][j+1]:
        sum += p

    #print(sum)
    return sum

'''c=hourglass(H,1,1)
print("Sum is:",c)
print(); */
#hourglass(H,2,2)'''

e = [][]
for i in range(1,3):
    for j in range(1,3):
        d = hourglass(H,i,j)
        e[i-1][j-1].append(d)
        print(d)

print(e)
        

