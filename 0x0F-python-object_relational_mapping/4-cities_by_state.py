#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
                   FROM states INNER JOIN cities ON states.id = cities.state_id
                   ORDER BY cities.id ASC""")
    all_cities = cursor.fetchall()
    for cities in all_cities:
        print(cities)
    cursor.close()
    db.close()
