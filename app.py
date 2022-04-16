#!python3.9

import os
import connection

import pandas as pd

if __name__ == "__main__":
    
    #list path
    path = os.getcwd()                      # os.getcwd()           ==>> masuk ke direktori kerja
    path_query = path + '/sql/'             # = os.getcwd("/sql")   ==>> masuk ke dalam folder "sql"

    #list filename
    file_query = 'dml_query.sql'        # memberikan variabel pada file dalam folder "sql"

    #connection
    conn = connection.db_connect()          # db_connect()          ==>> function di connection.py
    cur = conn.cursor()                     # cursor()              ==>> execute statement / communicate with my SQL

    # read data
    with open(path_query + file_query,'r') as file:
        query = file.read()
    cur.execute(query)                      # executes the given database  
    data =  cur.fetchall()                   # fetches all the rows of a query result. It returns all the rows as a list of tuples.
    # print(data)                           # raw data
    df = pd.DataFrame(data, columns=['order','review score','product category'])

    df \
        .groupby(['review score','product category']) \
        .agg({'order':'count'}) \
        .unstack() \
        .to_excel('report_review_score.xlsx')                     # export data ke dalam bentuk excel

    print(df.info())
    print(df)