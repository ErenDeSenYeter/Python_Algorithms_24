 #iterative binary search 

def binary_itr(arr,start, end, target):
    while start <= end:

        mid = ( start + end ) // 2
        print(mid)
        if arr[mid] < target:
            start = mid+1

        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
        
    return start
    #return -1

arr =[2,5,8,10,16,22,25]
target = 10

result = binary_itr(arr, 0, len(arr)-1, target)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")
    