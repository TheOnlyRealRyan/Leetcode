arr = [3,5,7,17,23,60,112,150,200,212,222,233,255]
arr2 = [3,5,7,17,23,60,112,150,200,212,222,233,255,300]
answer = 222
left = 0
right = len(arr)-1

def binSearch(left, right, answer, arr):
    while left < right:
        mid = (left+right)//2
        if answer == arr[mid]:
            return mid
        elif answer < arr[mid]:
            right = mid-1 
        elif answer > arr[mid]:
            left = mid+1
            
    return -1

print(binSearch(left, right, answer, arr2))