import sqlite3
conn = sqlite3.connect('ferrariofanclub.db')
c = conn.cursor()
def crate_table(tablename):
    match tablename:
        case 'user':
            sql = "CREATE TABLE user(username PRIMARY KEY, password)"
            
        case 'bank':
            sql = "CREATE TABLE bank(user PRIMARY KEY, kontostand)"

    c.execute(sql)
    conn.commit()


def check_if_table_exists(table_name):
    sql = 'SELECT * FROM ' + table_name
    try:
        c.execute(sql)
        return True
    except sqlite3.OperationalError:
        return False


def check_if_user_exists(username):
    a = "'"
    sql = 'SELECT * FROM user WHERE username = ' + a + username + a
    c.execute(sql)
    if c.fetchone() is not None:
        return True
    else:
        return False


def insert_user(username, password):
    if check_if_user_exists(username) == True:
        print("User existiert bereits.")
        return
    else:
        a = "'"
        print('INSERT INTO user (username, password) VALUES (' + a + username + a + ', ' + a + password + a + ')')
        c.execute('INSERT INTO user (username, password) VALUES (' + a + username + a + ', ' + a + password + a + ')')
        c.execute('INSERT INTO bank (user, kontostand) VALUES (' + a + username + a + ', 1000)')
        conn.commit()

def show_table(table_name):
    sql = 'SELECT * FROM ' + table_name
    print(sql)
    for row in c.execute(sql):
        print(row)

def updete_bank(username, amount):
    a = "'"
    c.execute('UPDATE bank SET kontostand = kontostand + (' + str(amount) + ') WHERE user = ' + a + username + a)
    conn.commit()

def delete_user(username):
    a = "'"
    c.execute('DELETE FROM user WHERE username = ' + a + username + a)
    c.execute('DELETE FROM bank WHERE user = ' + a + username + a)
    conn.commit()


if __name__ == "__main__":


    # cur is an sqlite3.Cursor object
    '''if check_if_table_exists('user') == False:
        c.executescript("""
            BEGIN;
            CREATE TABLE user(username, password);
            COMMIT;
        """)'''
    
    '''if check_if_table_exists('bank') == False:
        c.executescript("""
            BEGIN;
            CREATE TABLE bank(user, kontostand);
            COMMIT;
        """)'''

   
    show_table('user')
    show_table('bank')
    