def pairInSorted(arr,s,n):
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            break
    l=(i+1)%n
    r=i
    
    while(l!=r):
        if(arr[l]+arr[r]==s):
            return True
        
        elif(arr[l]+arr[r]>s):
            r=(n+r-1)%n
        else:
            l=(l+1)%n
        
    return False
        
if __name__=='__main__':
    arr=[11, 15, 26, 38, 9, 10]
    s=19
    print(pairInSorted(arr,s,len(arr)))
