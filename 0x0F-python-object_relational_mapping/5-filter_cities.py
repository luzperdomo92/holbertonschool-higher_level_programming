#!/usr/bin/python3
''' lists all cities of a particular state'''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities
                   INNER JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s ORDER BY cities.id""",
                   (argv[4], ))
    rows_select = cursor.fetchall()
    print(", ".join([row[0] for row in rows_select]))
    cursor.close()
    db.close()
