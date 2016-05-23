# coding=utf-8
import requests
import json

def daily_profit():
    r = requests.get("https://blockexplorer.com/api/status?q=getDifficulty")
    price_api = requests.get("https://api.bitcoinaverage.com/ticker/global/CNY/last")

    single_hs = float(raw_input('Please input the single machine hashrate:'))
    amount = int(raw_input('Please input the amount of machine:'))

    f = json.loads(r.text)
    e = f.get("difficulty")

    price = json.loads(price_api.text)

    block_time = (e * (2 ** 32)) / ((single_hs * amount) * (10 ** 12))
    time_hour = block_time/3600
    time_day = time_hour/24
    day_profit = 25/time_day

    day_gain = day_profit * price


    print round(time_day, 5),"\n", round(day_profit, 3),"\n", round(day_gain, 2)
    return round(day_gain, 2)


daily_profit()