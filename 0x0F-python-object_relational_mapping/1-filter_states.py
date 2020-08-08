#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the
    database hbtn_0e_0_usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * from states WHERE name LIKE 'N%'
                   COLLATE latin1_general_cs ORDER BY states.id""")
    state_list = cursor.fetchall()
    for state in state_list:
        print(state)
    cursor.close()
    db.close()
