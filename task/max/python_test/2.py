#!/usr/bin/python
str_profit=float(raw_input("please input profit...\n"))
print str_profit
if str_profit <=100000:
	print "bonus=",str_profit*0.1
elif str_profit>100000 and str_profit<=200000:
	print "bonus=",(str_profit-100000)*0.075+100000*0.1
elif str_profit>200000 and str_profit<=400000:
        print "bonus=",(str_profit-200000)*0.05+100000*0.075+100000*0.1
elif str_profit>400000 and str_profit<=600000:
        print "bonus=",(str_profit-400000)*0.03+200000*0.05+100000*0.075+100000*0.1
elif str_profit>600000 and str_profit<=1000000:
        print "bonus=",(str_profit-600000)*0.015+200000*0.03+200000*0.05+100000*0.075+100000*0.1
else: 
        print "bonus=",(str_profit-1000000)*0.01+400000*0.015+200000*0.03+200000*0.05+100000*0.075+100000*0.1



