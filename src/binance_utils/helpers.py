# -*- coding: utf-8 -*-
from collections import Counter
from decimal import Decimal


def filter_assets(asset_list):
    return [b for b in asset_list if Decimal(b['free']) > 0 or Decimal(b['locked']) > 0]


def filter_tickers(spot, tickers, base):
    return [t for t in tickers for s in spot if t['symbol'] == f"{s['asset']}{base}"]


def insert_currency_value(asset, currency, prices):
    try:
        return Decimal(asset['total']) * Decimal(
            next(iter((b for b in prices if b['symbol'] == f"{asset['asset']}{currency}")))['price']
        )
    except StopIteration:
        if asset['asset'] == currency:
            return asset['total']


def get_totals(assets):
    total = Counter()
    for a in assets:
        for k, v in a.items():
            try:
                total[k] += v
            except TypeError:
                pass
    return total

