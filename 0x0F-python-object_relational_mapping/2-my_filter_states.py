#!/usr/bin/python3
"""takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument."""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * from states WHERE name='{}'
                   ORDER BY states.id""".format(argv[4]))
    state_list = cursor.fetchall()
    for state in state_list:
        print(state)
    cursor.close()
    db.close()
