import sqlite3
import pandas as pd

timeframes = ['2015-01']

for timeframe in timeframes:
    connection = sqlite3.connect('{}.db'.format(timeframe))
    c = connection.cursor()
    limit = 5000
    last_unix = 0 # Buffer through date and grab last time stamp
    cur_length = limit
    counter = 0;
    test_done = False