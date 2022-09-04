"""You are given the power of the six infinity stones Tony Stark,
with the help of Jarvis, has found out 
a way to increase the total power of the infinity stones. 
The powers of the infinity stones are given by A,B,C,D,E,F. 
Tony has doubled the power of the stone with power B, 
while the power of stone C is increased by 3 times, 
and that of stone D is also increased by 3 times. 
The power of the stones with power E and F, 
has been doubled as well, while that of stone with power A is unchanged. 
Find the new total power of the stone."""

a,b,c,d,e,f = map(int,input().split())
x = a+b*2+c*3+d*3+e*2+f*2
print(x)