#!/usr/bin/python3
'''This script lists all states from the database hbtn_0e_0_usa'''
import MySQLdb
import sys


if __name__ == '__main__':

    data_base = MySQLdb.connect(host='localhost',
                                port=3306,
                                user=sys.argv[1],
                                passwd=sys.argv[2],
                                database=sys.argv[3])

    cur = data_base.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id')

    rows = cur.fetchall()
    for i in rows:
        print(i)

    cur.close()
    data_base.close()
