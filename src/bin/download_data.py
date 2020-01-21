import argparse 
import pandas as pd
import os
from .src.data_processing import iex_historical_fetch

def main(token, ticker, start, end, out_path):
    data = iex_historical_fetch(token, ticker, start, end, out_path)
    data.to_csv(out_path)

if __name__=="__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('token', type=str, help='iex api token')
    parse.add_argument('ticker', type=str, help="ticker symbol")
    parse.add_argument('start', type=str, help='start date of historical data in format yyyy-mm-dd')
    parse.add_argument('end', type=str, help='end date of historical data in format yyyy-mm-dd')
    parse.add_argument('out_path', type=str, help='absolute path of where to save the data.')
    args = parse.parse_args()

    main(args.token, args.ticker, args.start, args.end, args.out_path)