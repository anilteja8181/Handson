#!bin/bash
sum1=0
a=153
while ( a > 0 ):
	rem=(a%10)
	sum1=(sum1*10)+rem
	a=a/10
	continue
print("reverse of no is %d" %sum1)
