# -*- coding: utf-8 -*-
from decimal import Decimal
from tabulate import tabulate

from binance_utils.helpers import (
    filter_assets,
    filter_tickers,
    insert_currency_value,
    get_totals
)


def balances(client):
    spot = filter_assets(client.get_account()['balances'])
    tickers = client.get_all_tickers()
    btc_prices = filter_tickers(spot, tickers, 'BTC')
    busd_prices = filter_tickers(spot, tickers, 'BUSD')
    btcbusd = next(iter([t for t in tickers if t['symbol'] == 'BTCBUSD']))
    for s in spot:
        s['total'] = Decimal(s['free']) + Decimal(s['locked'])
        s['BUSD'] = insert_currency_value(s, 'BUSD', busd_prices)
        s['BTC'] = insert_currency_value(s, 'BTC', btc_prices)
        if s['asset'] == 'BTC':
            if s['BUSD'] is not None:
                raise ValueError
            s['BUSD'] = Decimal(s['BTC']) * Decimal(btcbusd['price'])
        if s['asset'] == 'BUSD':
            if s['BTC'] is not None:
                raise ValueError
            s['BTC'] = Decimal(s['BUSD']) / Decimal(btcbusd['price'])

    table = [{'Asset': s['asset'], 'Total': s['total'], 'BUSD': s['BUSD'], 'BTC': s['BTC']} for s in spot]
    totals = get_totals(table)
    print(tabulate(table, headers="keys", tablefmt="fancy_grid", numalign="right", floatfmt=".2f"))
    print()
    print(f'Totals: {totals["BUSD"]:,.2f} BUSD, {totals["BTC"]:,.2f} BTC')

