def get_sum(myList):
    sum = 0
    for row in myList:
        for item in row:
            sum += item
    return sum

print(get_sum([[1,2,3], [4,5,6]]))