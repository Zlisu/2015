import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()
    print("type of the fetchall result: ", type(rows))

    for row in rows:
        print(row)

def select_task_by_priority(conn, priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = 'C:\sqlite\db\pythonsqlite.db'

    conn = create_connection(database)
    with conn:
        print("1. priority 1 tasks: ")
        select_task_by_priority(conn, 1)

        print("2. all tasks: ")
        select_all_tasks(conn)

if __name__ == '__main__':
    main()
