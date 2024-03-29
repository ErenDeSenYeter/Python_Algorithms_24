#l = [1,3,6,7,9,12,13]

#implement naive search

def naive_search(l, target):
    for i in range(len(l)):
        if l[i]== target:
            return i 
        
    return -1 

def binary_search(l,target, low = None, high = None):
    if low is None:
        low = 0 
    if high is None:
        high = len(l) - 1
    if high < low :
        return -1

    #getting the midpoint 
    midpoint = (low + high) // 2 

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        new_high = midpoint -1 
        return binary_search(l,target,low,new_high)
    else:
        #targer > l[midpoint]
        new_low = midpoint + 1
        return binary_search(l,target,new_low,high) 
    

if __name__ == "__main__":
    l = [1,3,6,7,9,12,13]
    target = 12 
    print(naive_search(l,target))
    print(binary_search(l,target))