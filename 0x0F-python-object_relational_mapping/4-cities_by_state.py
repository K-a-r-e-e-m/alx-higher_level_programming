#!/usr/bin/python3
'''In this module we will lists all cities from the database hbtn_0e_4_usa'''
import MySQLdb
from sys import argv

if __name__ == '__main__':

    data_base = MySQLdb.connect(host='localhost',
                                port=3306,
                                user=argv[1],
                                passwd=argv[2],
                                database=argv[3])

    cur = data_base.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name\
                FROM cities JOIN states ON state_id = states.id')

    rows = cur.fetchall()
    for i in rows:
        print(i)

    cur.close()
    data_base.close()
