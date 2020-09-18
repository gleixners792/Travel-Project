#!/usr/bin/python
# coding: utf-8

import psycopg2
#from config import config

import numpy as np
from flask import Flask, jsonify, render_template, redirect
import datetime as dt

app = Flask(__name__)

""" Connect to the PostgreSQL database server """
conn = None
try:
    # read connection parameters
    # params = config()

    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect("dbname=Project3_TravelData user=postgres password=VW1985gti port=5432")

    # create a cursor
    cur = conn.cursor()

    # execute db commands
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print("I am here #1", db_version)

    cur.execute("SELECT * from city")
    cities = cur.fetchall()
    print("The number of Cities: ", cur.rowcount)
    for city in cities:
        print(city)

    print("jason data In")
    # jsonify does not work like this
    #city_data = []
    #city_data = jsonify(cities)
    #print("json data Out")
    #print(city_data)

    # close the communication with the PostgreSQL
    cur.close()

except (Exception, psycopg2.DatabaseError) as error:
     print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')


@app.route("/")
def index():
  return render_template("index.html", city_data=jsonify(cities))

#def welcome():
#    """List Some Data"""
#    return jsonify(cities)


if __name__ == '__main__':
    app.run(debug=True)
