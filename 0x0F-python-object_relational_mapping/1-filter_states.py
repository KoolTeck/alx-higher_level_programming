#!/usr/bin/python3
""" The 0-select_states.py module """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3])
        cur = conn.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            if row[1].startswith('N'):
                print(row)
        cur.close()
        conn.close()
    except Exception as err:
        print(err)
