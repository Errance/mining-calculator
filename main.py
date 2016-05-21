# def gross_profit(init_params = {}):


def initialize():

    init_params = {'electric_charge_rate': raw_input('Please input the electric charge rate:'),
                   'total_hash_rate': raw_input('Please input the total hashrate:'),
                   'single_machine_hashrate': raw_input('Please input the single machine hashrate:'),
                   'single_machine_power': raw_input('Please single machine power:'),
                   'machine_amount': raw_input('Please input the amount of machine:'),
                   'machine_price': raw_input('Please input the price of the machine:'),
                   'btc_price': raw_input('Please input the price of the bitcoin:')}

    # print init_params['']
    x = init_params.get('electric_charge_rate')
    y = init_params.get('total_hash_rate')
    z = init_params.get('single_machine_hashrate')
    a = init_params.get('single_machine_power')
    b = init_params.get('machine_amount')
    c = init_params.get('machine_price')
    d = init_params.get('btc_price')
    btc_per_block = 25

    total_cost_machine = float(c) * float(b)
    print total_cost_machine
    daily_electric_fee = ((float(x)*int(a)*int(b))/1000)*24
    print daily_electric_fee
    daily_btc_profit = (float(z)*int(b)/(1000*int(y))) * 144 * btc_per_block * int(d)
    print daily_btc_profit
    gross_profit = daily_btc_profit - daily_electric_fee
    print gross_profit
    days = total_cost_machine/gross_profit
    print days
    return days


initialize()




