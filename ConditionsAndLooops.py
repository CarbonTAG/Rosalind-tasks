# This script adds up all odd numbers ranging from a to b all inclusive
#================My solution============================================
odd_n = []
total = 0

def odd(a,b):
    """This appends odd numbers to a list of odd numbers ranging from a to b."""
    for i in range(a,b+1):
        if i % 2 != 0:
            odd_n.append(i)

odd(1, 9)

# this loop adds all the odd numbers
for n in odd_n:
    total += n


#print(odd_n)
print(total)

#======================== their psuedo solution==================================
#sum=0
#for i=a; i<=b; i++
#  if i%2==1
#    sum+=i


#print(sum)
