# My thinking:
# optimisation options are:
# linked list?
# but probably hashmap
# but i havent learnt that yet

# search lowest to highest (n^2 complexity)
# for i for j  


def alg(array):
    value = 0
    position = 0
    if len(array) <=1:
        return "invalid"
    for i in range(len(array)-1):
        for j in ( range(i+1, len(array)-1)):
            if array[i] < array[j] and array[j]-array[i] > value:
                value = array[j]-array[i]
                position = [i, j]
            elif value == 0:
                value = 0
                position = 0
    return position, value

# array = [7,6,4,3,1]
# array = [1]
array = [7,1,5,3,6,4]

print(alg(array))
            