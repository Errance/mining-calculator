# coding=utf-8
import requests
import json


def initialize(amount):
    init_params = {'electric_charge_rate': raw_input('Please input the electric charge rate:'),
                   'single_machine_power': raw_input('Please single machine power:'),
                   'machine_price': raw_input('Please input the price of the machine:')}
    # 'machine_amount': raw_input('Please input the amount of machine:'),
    # 'btc_price': raw_input('Please input the price of the bitcoin:')}
    # 'total_hash_rate': raw_input('Please input the total hashrate:'),
    # 'single_machine_hashrate': raw_input('Please input the single machine hashrate:'),

    # print init_params['']
    x = init_params.get('electric_charge_rate')
    a = init_params.get('single_machine_power')
    c = init_params.get('machine_price')
    # b = init_params.get('machine_amount')
    # y = init_params.get('total_hash_rate')
    # z = init_params.get('single_machine_hashrate')
    # d = init_params.get('btc_price')

    elec_fee = float(x) * (float(a) / 1000)  # electric fee per hour
    total_elec = elec_fee * amount * 24  # total electric fee per hour

    price = amount * float(c)
    data_out = {"Daily fee" : round(total_elec, 2), "Machine Price" : price}

    print "The total price of the machines are: %d" % price

    return data_out.get("Daily fee"), data_out.get("Machine Price")