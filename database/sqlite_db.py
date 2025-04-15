import sqlite3

def search_add_new_user_db(new_user_data, type_add_or_search): #tg_id, first_name, last_name, username, date):
    connection =sqlite3.connect('vip_user.db')

    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS vip_users (id INTEGER PRIMARY KEY AUTOINCREMENT, " \
    "user_tg_id INTEGER NOT NULL UNIQUE," \
    "first_name TEXT," \
    "last_name TEXT, " \
    "username TEXT, " \
    "date_of_added TEXT);")

    cursor.execute('SELECT user_tg_id FROM vip_users WHERE user_tg_id = ?', (new_user_data[0],))
    existing_user = cursor.fetchone()
    if type_add_or_search == 1: #add
        if existing_user is None:  
            cursor.execute("INSERT INTO vip_users(user_tg_id, first_name, last_name, username, date_of_added) VALUES (?, ?, ?, ?, ?)",
                        (new_user_data[0], new_user_data[1], new_user_data[2], new_user_data[3], new_user_data[4]))
            connection.commit()
        connection.close()
    elif type_add_or_search == 2:#search
        if existing_user is None:  
            connection.close()
            return False
        else:
            connection.close()
            return True
    

    
        
   
    
    

