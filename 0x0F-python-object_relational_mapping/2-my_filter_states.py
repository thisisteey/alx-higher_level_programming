#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        dbconn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
        )
        dbcur = dbconn.cursor()
        stname = sys.argv[4]
        dbqry = (
            f'SELECT * FROM states WHERE CAST(name AS BINARY) LIKE ' +
            f'CAST("{stname}" AS BINARY) ORDER BY id ASC;'
        )
        dbcur.execute(dbqry)
        qryres = dbcur.fetchall()
        for row in qryres:
            print(row)
        dbconn.close()
