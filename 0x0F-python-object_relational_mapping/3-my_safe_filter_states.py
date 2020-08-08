#!/usr/bin/python3
# write one that is safe from MySQL injections!
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * from states WHERE name=%s
                   ORDER BY states.id""", (argv[4], ))
    state_list = cursor.fetchall()
    for state in state_list:
        print(state)
    cursor.close()
    db.close()
