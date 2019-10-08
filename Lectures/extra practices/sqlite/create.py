import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    # When you connect to an SQLite database file that does not exist, 
    # SQLite automatically creates a new database for you.
    try:
        conn = sqlite3.connect(db_file)  # creates a Connection object
    except Error as e:
        print(e)
        
    return conn  # returns a Connection object

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"c:\sqlite\db\pythonsqlite.db"
    
    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS projects (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    begin_date text,
                                    end_date text
                                );"""
    
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                priority integer,
                                project_id integer NOT NULL,
                                status_id integer NOT NULL,
                                begin_date text NOT NULL,
                                end_date text NOT NULL,
                                FOREIGN KEY (project_id) REFERENCES projects (id)
                            );"""
    
    conn = create_connection(database)
    
    if conn is not None:
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error!")
        
if __name__ == '__main__':
    main()