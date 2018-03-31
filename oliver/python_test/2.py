#!/usr/bin/python

profit_str = raw_input("please iput your profit\n")
profit = int(profit_str)
if profit <= 100000:
	bonus = profit * 0.1
	print "bonus is " + str(bonus)
elif profit > 100000 and profit <= 200000:
	bonus = (profit - 100000) * 0.075
        bonus += 100000 * 0.1
	print "bonus is " + str(bonus)
elif profit > 200000 and profit <= 400000:
	bonus = (profit - 200000) * 0.05
        bonus += 100000 * 0.75
        bonus += 100000 * 0.1
	print "bonus is " + str(bonus)
elif profit > 400000 and profit <= 600000:
	bonus = (profit - 400000) * 0.03
        bonus += 200000 * 0.05
        bonus += 100000 * 0.75
        bonus += 100000 * 0.1
        print "bonus is " + str(bonus)
elif profit > 600000 and profit <= 1000000:
	bonus = (profit - 600000) * 0.015
        bonus += 200000 * 0.03
        bonus += 200000 * 0.05
        bonus += 100000 * 0.75
        bonus += 100000 * 0.1
        print "bonus is " + str(bonus)
elif profit > 1000000:
	bonus = (profit - 1000000) * 0.01
        bonus += 400000 * 0.015
        bonus += 200000 * 0.03
        bonus += 200000 * 0.05
        bonus += 100000 * 0.75
        bonus += 100000 * 0.1
        print "bonus is " + str(bonus)
        
	
        	
