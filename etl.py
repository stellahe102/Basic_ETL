import os
import glob
import pandas as pd

# get a list of all JSON files
all_json_files = list()
root_path = 'data/song'
for root, dirs, files in os.walk(root_path):
    files = glob.glob(os.path.join(root, '*.json'))
    for file in files:
        all_json_files.append(os.path.abspath(file))
print('{} files are found in path {}'.format(len(all_json_files, root)))



# create database
# connect to new database
import psycopg2
conn = psycopg2.connect("host=127.0.0.1, dbname=studentdb, user=postgres password = admin")
conn.set_session(autocommit=True)
cur = conn.cursor()

cur.execute("DROP DATABASE IF EXISTS songdb")
cur.execute("CREATE DATABASE songdb WITH ENCODING 'utf8' TEMPLATE template0")

conn.close()

conn = psycopg2.connect("host=127.0.0.1, dbname=songdb, user=postgres password = admin")
cur = conn.cursor()


# function to drop tables
# function to execute to drop tables


# function to execute to create tables
# function to create tables


# function to execute to insert data
# function to insert data