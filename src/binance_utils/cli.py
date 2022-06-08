# -*- coding: utf-8 -*-
import logging
import typer
import os
from binance.client import Client
from binance_utils.reports import balances


logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger('')
logger.setLevel(logging.INFO)

app = typer.Typer()

api_key = os.environ['BINANCE_KEY']
api_secret = os.environ['BINANCE_SECRET']


@app.command('balances')
def build_status():
    client = Client(api_key, api_secret)
    balances(client)


def main():
    app()
