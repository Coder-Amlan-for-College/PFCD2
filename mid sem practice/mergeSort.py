def merge(arr,left,mid,right):
    merged = [0]*(right-left+1)
    idx1 = left
    idx2 = mid+1
    x=0
    while idx1<=mid and idx2<=right:
        if(arr[idx1]<arr[idx2]):
            merged[x] = arr[idx1]
            idx1 += 1
        else:
            merged[x]=arr[idx2]
            idx2 += 1
        x += 1
    while idx1<=mid:
        merged[x] = arr[idx1]
        x+=1
        idx1+=1
    while idx2<=right:
        merged[x] = arr[idx2]
        x+=1
        idx2+=1
    
    for i in range(len(merged)):
        arr[left+i] = merged[i]
    
def mergeSort(arr,left,right):
    if left>=right:
        return
    
    mid = left+(right-left)//2
    mergeSort(arr,left,mid)
    mergeSort(arr,mid+1,right)
    merge(arr,left,mid,right)


arr = [5,4,3,2,1]
mergeSort(arr,0,4)
print(arr)