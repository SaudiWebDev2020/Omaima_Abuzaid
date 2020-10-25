## Print all integers from 0 to 150.
for i in range (0,151,1):
    print(i)
## Print all the multiples of 5 from 5 to 1,000
x=5
while x <=1000:
    print(x)
    x= x*5

##Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for n in range (1,101):
    if n%5==0:
        print ('coding')
    if n%10==0:
        print('Coding Dojo')
    else:
        print (n)
##Add odd integers from 0 to 500,000, and print the final sum.
final_sum=0
for y in range (500,000):
    if y % 2 ==1:
        final_sum= y+final_sum
        print(y, 'the sum is', final_sum)
##Print positive numbers starting at 2018, counting down by fours.
for t in range (2018,0,-4):
    if t % 2 == 0:
        print(t)
##Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lownum = 2
highnum = 30
mult =3
for i in range (lownum, highnum+1):
    if (i % mult == 0):
        print (i)
    