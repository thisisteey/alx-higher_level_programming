#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) >= 5:
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
            'SELECT cities.name FROM cities ' +
            'INNER JOIN states ON cities.state_id = states.id ' +
            'WHERE CAST(states.name AS BINARY) = %s ' +
            'ORDER BY cities.id ASC;'
        )
        dbcur.execute(dbqry, ('%' + stname + '%',))
        qryres = dbcur.fetchall()
        print(', '.join(city[0] for city in qryres))
        dbconn.close()
