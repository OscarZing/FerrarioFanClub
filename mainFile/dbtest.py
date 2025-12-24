import sqlite3
conn = sqlite3.connect('ferrariofanclub.db')
c = conn.cursor()
def create_table(tablename):
    if check_if_table_exists(tablename) == True:
        print("Tabelle " + tablename + " existiert bereits.")
        return
    else:
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
    if c.fetchone() is None:
        return False
    else:
        return True


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


    insert_user('1234', '1234') 
    delete_user('123')
    show_table('user')
    show_table('bank')
    