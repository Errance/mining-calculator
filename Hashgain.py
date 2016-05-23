# coding=utf-8
import requests
import json


def daily_profit(amount):

    r = requests.get("https://blockexplorer.com/api/status?q=getDifficulty")
    price_api = requests.get("https://api.bitcoinaverage.com/ticker/global/CNY/last")

    single_hs = float(raw_input("Please input the single machine hashrate:"))

    f = json.loads(r.text)
    e = f.get("difficulty")

    price = json.loads(price_api.text)

    # How long you will mined one block in second
    block_time = (e * (2 ** 32)) / ((single_hs * amount) * (10 ** 12))
    # time_hour = block_time / 3600
    # How long you will mined one block in day
    time_day = block_time / (24*3600)
    day_profit = 25 / time_day

    day_gain = day_profit * price

    print "You will mine 1 block in %.2f days" % round(time_day, 2)
    print "You will gain %.2f BTC in one day" % round(day_profit, 2)

    return round(day_gain, 2)
