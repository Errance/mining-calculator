# coding=utf-8
import requests
import json
import Cost
import Hashgain

amount = int(raw_input('Please input the amount of machine:'))

x = Cost.initialize(amount)
y = float(Hashgain.daily_profit(amount))

print y - float(x[0])

days = float(x[1])/(y - float(x[0]))

print days