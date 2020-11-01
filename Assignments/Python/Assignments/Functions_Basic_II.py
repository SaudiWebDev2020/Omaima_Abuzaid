
#Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown (counter):
    new_list=[]
    for a in range(counter,-1,-1):
        new_list.append (a)
    return new_list
print (countdown(10))

##Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return (a):
    print(a[0])
    return (a[1])
print(print_and_return([1,2]))

#Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length (_list):
    return _list[0]+ len(_list)

print(first_plus_length([3,3,5,6,8]))

##Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def values_greater_than_second (_list):
    if (len(_list) > 1):
        new_list=[]
        for a in _list:
            if a > _list[1]:
                new_list.append(a)
        return new_list
    else:
        return False
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))

##Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_and_value (size, val):
    new_list=[]
    for a in range(size):
        new_list.append(val)
        return new_list
print(length_and_value(4,5))
