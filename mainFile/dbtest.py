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
                sql = "CREATE TABLE user(username PRIMARY KEY, password, betrunkenheit DEFAULT 0)"
                
            case 'bank':
                sql = "CREATE TABLE bank(user PRIMARY KEY, kontostand, schulden DEFAULT 0)"
            
            case "casino":
                sql = "CREATE TABLE casino(user PRIMARY KEY, )"
            
            case "drinks":
                sql = "CREATE TABLE drinks(nummer, drinkname PRIMARY KEY, preis, alkoholgehalt, menge)"

    c.execute(sql)
    conn.commit()
 
def delete_table(tablename):
    if check_if_table_exists(tablename) == False:
        print("Tabelle " + tablename + " existiert nicht.")
        return
    else:
        sql = 'DROP TABLE ' + tablename
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

def check_password(username, password):
    a = "'"
    sql = 'SELECT * FROM user WHERE username = ' + a + username + a + ' AND password = ' + a + password + a
    c.execute(sql)
    if c.fetchone() is None:
        return False
    else:
        return True

def insert_drink(nummer, drinkname, preis, alkoholgehalt, menge):
    a = "'"
    c.execute('INSERT INTO drinks (nummer, drinkname, preis, alkoholgehalt, menge) VALUES (' + str(nummer) + ', ' + a + drinkname + a + ', ' + str(preis) + ', ' + str(alkoholgehalt) + ', ' + str(menge) + ')')
    conn.commit()

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

def get_all_drinks():
    sql = 'SELECT * FROM drinks'
    c.execute(sql)
    drinks = c.fetchall()
    return drinks

def get_all_numbers():
    sql = 'SELECT nummer FROM drinks'
    c.execute(sql)
    numbers = c.fetchall()
    return numbers

def get_price(nummer):
    sql=('SELECT preis FROM drinks WHERE nummer = ' + str(nummer))
    c.execute(sql)
    price = c.fetchone()
    return int(price[0])

def get_alcohol_content(nummer):
    a = "'"
    sql=('SELECT alkoholgehalt FROM drinks WHERE nummer = ' + str(nummer))
    c.execute(sql)
    alcohol_content = c.fetchone()
    return float(alcohol_content[0])

def get_volume(nummer):
    a = "'"
    sql=('SELECT menge FROM drinks WHERE nummer = ' + str(nummer))
    c.execute(sql)
    volume = c.fetchone()
    return int(volume[0])

def get_drinkname(nummer):
    a = "'"
    sql=('SELECT drinkname FROM drinks WHERE nummer = ' + str(nummer))
    c.execute(sql)
    drinkname = c.fetchone()
    return str(drinkname[0])

def get_balance(username):
    a = "'"
    sql=('SELECT kontostand FROM bank WHERE user = ' + a + username + a)
    c.execute(sql)
    balance = c.fetchone()
    return int(balance[0])

def get_debt(username):
    a = "'"
    sql=('SELECT schulden FROM bank WHERE user = ' + a + username + a)
    c.execute(sql)
    debt = c.fetchone()
    return int(debt[0])

def update_bank(username, amount):
    a = "'"
    c.execute('UPDATE bank SET kontostand = kontostand + (' + str(amount) + ') WHERE user = ' + a + username + a)
    conn.commit()

def update_debt(username, amount):
    a = "'"
    c.execute('UPDATE bank SET schulden = schulden + (' + str(amount) + ') WHERE user = ' + a + username + a)
    conn.commit()


def reset_balance(username):
    a = "'"
    c.execute('UPDATE bank SET kontostand = 1000 WHERE user = ' + a + username + a)
    conn.commit()

def delete_user(username):
    a = "'"
    c.execute('DELETE FROM user WHERE username = ' + a + username + a)
    c.execute('DELETE FROM bank WHERE user = ' + a + username + a)
    conn.commit()

def delete_all_users():
    c.execute('DELETE FROM user')
    c.execute('DELETE FROM bank')
    conn.commit()

if __name__ == "__main__":
    
    
    
    
    
    
    
    
    
    
    
    
    
    """delete_table('drinks')
    create_table('drinks')
    insert_drink('1', 'Bier', '5', '4.8', '50')
    insert_drink('2', 'Bier klein', '5', '4.8', '33')
    insert_drink('3', 'Wein', '7', '12.5', '10')
    insert_drink('4', 'Whisky', '15', '40.0', '2')
    insert_drink('5', 'Wodka', '12', '37.5', '2')
    insert_drink('6', 'cocktail', '10', '15.0', '4') --- Drinks debug und so, nicht löschen! ---""" 

    



    