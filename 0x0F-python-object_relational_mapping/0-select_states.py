#!/usr/bin/python3
''' lists all states from database hbtn_0e_0_usa'''
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * from states ORDER BY state.id ASC")
    state_list = cursor.fetchall()
    for state in state_list:
        print(state)
    cursor.close()
    db.close()
