def bs(arr,left,right,key):
    if left>right:
        return -1
    
    mid = left+(right-left)//2
    if(arr[mid]<key):
        return bs(arr,mid+1,right,key)
    elif(arr[mid]>key):
        return bs(arr,right,mid-1,key)
    else:
        return mid

arr = [1,2,3,4,5]
print(bs(arr,0,4,5))