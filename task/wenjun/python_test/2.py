#!/usr/bin/python

liru = 0.0
monney = 0
monney_str = raw_input("write monney\n")
monney = int(monney_str)

if monney <= 100000 :
	liru = monney*0.1;
elif monney>100000 and monney<=200000 :
	liru = 100000*0.1 + (monney-100000)*0.075;
elif monney>200000 and monney<= 400000 :
	liru = 100000*0.1 + 100000*0.075 + (monney-200000)*0.05
elif monney>400000 and monney<= 600000:
	liru = 100000*0.1 + 100000*0.075 + 200000*0.05 + (monney-400000)*0.03;
elif monney>600000 and monney<=1000000:
	liru = 100000*0.1 + 100000*0.075 + 200000*0.005 + 200000*0.03 + (monney-600000)*0.015;
elif monney>1000000:
	liru = 100000*0.1 + 100000*0.075 + 200000*0.005 + 200000*0.03 + 400000*0.015 + (monney-1000000)*0.01;




print liru
