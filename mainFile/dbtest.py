import sqlite3
conn = sqlite3.connect('ferrariofanclub.db')
c = conn.cursor()

def check_if_table_exists(table_name):
    try:
        c.execute("SELECT * FROM {table_name}")
        return True
    except sqlite3.OperationalError:
        return False

def insert_user(username, password):
    a = "'"
    print('INSERT INTO user (username, password) VALUES (' + a + username + a + ', ' + a + password + a + ')')
    c.execute('INSERT INTO user (username, password) VALUES (' + a + username + a + ', ' + a + password + a + ')')
    conn.commit()

def show_table(table_name):
    for row in c.execute('SELECT * FROM ' + table_name):
        print(row)





if __name__ == "__main__":
    insert_user('testuser', 'testpass')
    show_table('user')
    # cur is an sqlite3.Cursor object
    if check_if_table_exists('user') == False:
        c.executescript("""
            BEGIN;
            CREATE TABLE user(username, password);
            COMMIT;
        """)
    
    if check_if_table_exists('bank') == False:
        c.executescript("""
            BEGIN;
            CREATE TABLE bank(user, kontostand);
            COMMIT;
        """)

