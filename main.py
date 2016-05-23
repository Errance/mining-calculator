# coding=utf-8
import requests
import json
import Cost
import Hashgain

amount = int(raw_input('Please input the amount of machine:'))

x = Cost.initialize(amount)
y = float(Hashgain.daily_profit(amount))
days = float(x[1])/(y - float(x[0]))

print "Your net profit per day is %.2f" % (y - float(x[0]))
print "Your gross profit is %.2f " % y
print "The first profit will be got after %.1f days" % days
