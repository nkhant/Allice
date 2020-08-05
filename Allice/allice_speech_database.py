import sqlite3
import json
from datetime import datetime #simple outputs to tell where we are at the time

timeframe = '2015-01'
sql_transaction = [] # When working with large data you want to build up a big transaction and do all at once

connection = sqlite3.connect('{}.db'.format(timeframe))
c = connection.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS parent_reply
    (parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, 
    parent TEXT, comment TEXT, subreddit TEXT, unix INT, score INT)""")

if _name_== "_main_":
    create_table()
    row_counter = 0
    paired_rows = 0