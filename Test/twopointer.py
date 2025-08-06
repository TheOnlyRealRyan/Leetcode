arr = [3,5,7,17,23,60,112,150,200,212,222,233,255]
left = 0
right = len(arr)-1

def pointer(left, right, arr):
    print('hello')
    while left < right:
        print(arr[left])
        print(arr[right])
        left+=1
        right-=1
        
pointer(left, right, arr)