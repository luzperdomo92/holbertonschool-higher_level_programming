#!/usr/bin/python3
# write one that is safe from MySQL injections!


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * from states WHERE name LIKE %s
                   ORDER BY states.id""", (argv[4], ))
    state_list = cursor.fetchall()
    for state in state_list:
        print(state)
    cursor.close()
    db.close()
