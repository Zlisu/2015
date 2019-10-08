import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = '''INSERT INTO projects(name, begin_date, end_date) VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid

def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = '''INSERT INTO tasks(name, priority, status_id, project_id, begin_date, end_date)
                VALUES(?,?,?,?,?,?)'''

    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)

    # 在create.py 运行之后, pythonsqlite.db 中已经有了 project table 和 task table
    # 所以下面可以直接向这两个 table 中输入 entries
    with conn:
        # create a new project
        project = ('Cool App with SQLite and Python', '2019-10-08', '2019-10-09')
        project_id = create_project(conn, project)

        # tasks
        task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2019-10-08', '2019-10-09')
        task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2019-10-08', '2019-10-09')

        # create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)

if __name__ == '__main__':
    main()