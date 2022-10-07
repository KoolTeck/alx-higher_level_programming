#!/usr/bin/python3
""" The 0-select_states.py module """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3])
        cur = conn.cursor()
        query = """SELECT * \
                  FROM `states` \
                  WHERE `name` = %s"""
        cur.execute(query, (argv[4],))
        query_rows = cur.fetchall()
        for state in query_rows:
            print(state)
        cur.close()
        conn.close()
    except Exception as err:
        print(err)
