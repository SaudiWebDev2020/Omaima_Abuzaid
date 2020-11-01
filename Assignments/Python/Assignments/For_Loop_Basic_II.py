##Given a list, write a function that changes all positive numbers in the list to "big".
def biggie_size (arr):
    for x in range(len(arr)):
        if arr[x] > 0:
            arr[x]='big'
    return arr

##print (biggie_size(arr=[1,-2,3,4,5,-8,9,-9,-4]))

##Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
def count_positives (lis):
    counter=0 
    for x in range (len(lis)):
        if (lis[x] > 0) :
            counter +=1
        lis[len(lis)-1]=counter
    
    return lis


##print(count_positives([-1, 1, 1, 1]))
##print(count_positives([1, 6, -4, -2, -7, -2])) 

##Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
def sum_total (arr):
    total=0
    for x in arr:
        total+=x
    return total

##print(sum_total(arr=[1,2,3,4]))

##Average - Create a function that takes a list and returns the average of all the values.x
def average (arr):
    avg=0
    for x in (arr):
        x+=1
        avg= (x+x)/len(arr)
    
    return avg
##print (average(arr=[1,2,3,4]))

##Length - Create a function that takes a list and returns the length of the list.
def length (lis):
    for x in range(len(lis)):
        x+=1
    return len(lis)
##print(length(lis=[37,2,1,-9]))

##Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def mini (arr):
    if (len(arr)>0):
        mini=arr[0]
        for x in range(len(arr)):
            if (arr[x]<mini):
                mini=arr[x]
        return mini
    else:
        print('False')

##print ([37,2,1,-9])


def maxi (arr):
    if (len(arr)>0):
        maxi=arr[0]
        for x in range(len(arr)):
            if (arr[x]>maxi):
                maxi=arr[x]
        return maxi
    else:
        print('False')

##print ([37,2,1,-9])
##print ([])

##Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis (arr):
    dic={}
    dic['sumTotal',sum_total(arr)]
    dic['average', average(arr)]
    dic['minimum', mini(arr)]
    dic['maximum',maxi(arr)]
    dic['length', length(arr)]
    return dic
print(ultimate_analysis([37, 2, 1, -9]))

