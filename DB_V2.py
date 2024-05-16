import sqlite3

def create_connection():
    return sqlite3.connect('foldersDB.db')

def craet_all_tables():
    create_table()
    create_table_of_Folders()

def create_table_of_Folders():
    conn = create_connection()
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS folderNames (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        folder_name TEXT NOT NULL
    );
    '''
    cursor.execute(create_table_query)

    conn.commit()
    conn.close()

def check_folder_exist_in_folderNames_table(foldername):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM folderNames WHERE folder_name=?", (foldername,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def insert_folder_name(folder_name):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO folderNames (folder_name) VALUES (?);", (folder_name,))

    conn.commit()
    conn.close()

def delete_row_by_foldername(foldername):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM folderNames WHERE folder_name=?", (foldername,))        
        conn.commit()
    except sqlite3.Error as e:
        print("Error removing row(s):", e)
    finally:
        conn.close()

def select_all_data():
    conn = create_connection()
    cursor = conn.cursor()

    select_query = 'SELECT * FROM folderNames'
    cursor.execute(select_query)

    rows = cursor.fetchall()

    conn.close()

    return rows

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ScansData (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT UNIQUE,
                        Schedule TEXT,
                        LastModify TEXT,
                        FolderName TEXT,
                        Description TEXT,
                        Target TEXT
                    )''')
    conn.commit()
    conn.close()

def get_all_data():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ScansData")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_data(name, schedule, last_modify, folder_name, description, target):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO ScansData (Name, Schedule, LastModify, FolderName, Description, Target)
                      VALUES (?, ?, ?, ?, ?, ?)''',
                   (name, schedule, last_modify, folder_name, description, target))
    conn.commit()
    conn.close()

def check_folder_exist(folder_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ScansData WHERE FolderName=?", (folder_name,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def check_name_exist(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ScansData WHERE Name=?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def get_data_by_folder_name(folder_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ScansData WHERE FolderName=?", (folder_name,))
    data = cursor.fetchall()
    conn.close()
    return data

def remove_scan_by_name(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ScansData WHERE Name=?", (name,))
    conn.commit()
    conn.close()

def remove_scan_by_folder_name(folder_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ScansData WHERE FolderName=?", (folder_name,))
    conn.commit()
    conn.close()

def get_scan_by_name(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ScansData WHERE Name=?", (name,))
    scan = cursor.fetchone()
    conn.close()
    return scan

def check_if_scans_exist():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ScansData")
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0

def rename_folder(old_folder_name, new_folder_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE ScansData SET FolderName=? WHERE FolderName=?", (new_folder_name, old_folder_name))
    cursor.execute("UPDATE folderNames SET folder_name=? WHERE folder_name=?", (new_folder_name, old_folder_name))
    conn.commit()
    conn.close()


# print(get_data_by_folder_name("All"))


# print(select_all_data())

# print(check_folder_exist_in_folderNames_table('Test 1'))

# create_table()

# data = get_all_data()
# print(data[0])

# for i in data:
#     print(i[1])

# print(get_scan_by_name("Scan1")[6])



# insert_folder_name("Scan 1")
# insert_folder_name("Scan 2")
# insert_folder_name("Scan 3")
# insert_folder_name("Scan 4")
# insert_data("Tiba"             , "Daily", "2024-03-18", "Scan 1" ,"Description of Tiba"              ,"https://portal.tiba.edu.eg")
# insert_data("Test"             , "Daily", "2024-03-18", "Scan 1" ,"Description of Test"              ,"http://test.com")
# insert_data("Test 2"           , "Daily", "2024-03-18", "Scan 1" ,"Description of Test 2"            ,"http://test2.net")
# insert_data("IT Gate Academy"  , "Daily", "2024-03-18", "Scan 2" ,"Description of IT Gate Academy"   ,"https://itgate.academy.com")
# insert_data("IT Gate Academy2" , "Daily", "2024-03-18", "Scan 2" ,"Description of IT Gate Academy 2" ,"https://itgate2.academy.com")
# insert_data("Al Salam Caffe"   , "Daily", "2024-03-18", "Scan 2" ,"Description of Al Salam Caffe"    ,"192.168.1.1")
# insert_data("Home"             , "Daily", "2024-03-18", "Scan 2" ,"Description of Home"              ,"192.168.1.1")
# insert_data("Home 2"           , "Daily", "2024-03-18", "Scan 3" ,"Description of Home 2"            ,"192.168.0.1")
# insert_data("Amazon"           , "Daily", "2024-03-18", "Scan 3" ,"Description of Amazon"            ,"www.amazon.com")
# insert_data("Vodafone"         , "Daily", "2024-03-18", "Scan 3" ,"Description of Vodafone"          ,"https://vodafone.com")
# insert_data("We Telecome"      , "Daily", "2024-03-18", "Scan 3" ,"Description of We Telecome"       ,"https://we.telecome.com")
# insert_data("Etisalat"         , "Daily", "2024-03-18", "Scan 3" ,"Description of Etisalat"          ,"https://etisalat.com")
# insert_data("Orange"           , "Daily", "2024-03-18", "Scan 3" ,"Description of Orange"            ,"https://orange.com")