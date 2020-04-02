#Leviston/edit Problem
#Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.
#Insert
#Remove
#Replace
#All of the above operations are of equal cost.


#Recursion BAsed Answer
def mindistance(s1,m,s2,n):
    if m==0:
        return n
    if n==0:
        return m
    if s1[m-1]==s2[n-2]:
        cost=0
    else:
        cost=1
    return min(mindistance(s1,m-1,s2,n)+1,
                mindistance(s1,m,s2,n-1)+1,
                mindistance(s1,m-1,s2,n-1)+cost)
if __name__ == '__main__':
    print(mindistance("alpha",5,"palpha",6))
    
    
# Since it has both recursion and overlapping problem then Dynamic programming can be applied

#Dynamic programmingbased approach

def mindistancedynamic(s1,s2):
    x=len(s1)
    y=len(s2)
    a=[[-1 for i in range(x)] for j in range(y)]
    for i in range(x):
        a[0][i]=i
    for j in range(y):
        a[i][0]=j
    for i in range(1,y):
        for j in range(1,x):
            if s1[j-1]==s2[i-1]:
                a[i][j]=a[i-1][j-1]
            else:
                a[i][j]=min(a[i-1][j]+1,
                            a[i][j-1]+1,
                            a[i-1][j-1]+1)
                            
    return a[y-1][x-1]
    
    
    if __name__ == '__main__':
        print(mindistancedynamic("bitting","likking"))