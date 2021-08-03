def get_sum(myList):
    sum = 0
    for item in myList:
        sum = sum + item
    return sum

myList = [1,2,3,4,5]

print(get_sum(myList))