#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                   FROM cities \
                   JOIN states ON cities.state_id = states.id \
                   WHERE states.name = %s \
                  ORDER BY cities.id""", (argv[4],))
    city_names = cur.fetchall()
    length = len(city_names) - 1
    for i in range(length):
        for name in city_names[i]:
            print(name, end=', ')
    try:
        print(city_names[length][0], end='')
    except Exception:
        pass
    print()
    cur.close()
    db.close()
