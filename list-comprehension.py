#first create an empty list
my_list = []

#iterate over the numbers 0 - 4 using the range() function
#range(5) creates an iterable, starting from 0 up to (but not including) 5
#Use the .append() method to add the numbers 0 - 4 to my_list

for num in range(5):
    my_list.append(num)

#print my_list
print(my_list)

#output
#[0, 1, 2, 3, 4]

#----------------------------------------------------------------------------------------

#initial list of numbers
numbers = [1,2,3,4,5,6]

#create a new,empty list to hold their squares
square_numbers = [num * num for num in numbers]

#iterate over initial list
#multiply each number by itself
#use .append() method, to add the square to the new list, square_numbers
"""
for num in numbers: 
    square_numbers.append(num * num)"""

#print new list
print(square_numbers)

#output
#[1, 4, 9, 16, 25, 36]

#----------------------------------------------------------------------------------------

new_list = [num for num in range(50) if num % 2 == 0]

print(new_list)

#output
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]

#----------------------------------------------------------------------------------------

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list1=[]
    for a in range(0,x+1):
        for b in range(0,y+1):
            for c in range(0,z+1):
                if a+b+c!=n:
                    list1.append([a,b,c])
    print(list1)