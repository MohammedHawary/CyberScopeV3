import sqlite3
import json
import os 
from datetime import datetime

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(CURRENT_DIR, 'vulnerability_scanner.db')


def create_tables():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            role TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Folders (
        folder_id INTEGER PRIMARY KEY AUTOINCREMENT,
        folder_name TEXT NOT NULL,
        user_id INTEGER,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES Users(user_id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Scans (
        scan_id INTEGER PRIMARY KEY AUTOINCREMENT,
        scan_name TEXT NOT NULL,
        user_id INTEGER,
        folder_id INTEGER,
        description TEXT NOT NULL,
        target_ip TEXT NOT NULL,
        status TEXT NOT NULL,
        scan_type TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        started_at TIMESTAMP,
        completed_at TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES Users(user_id),
        FOREIGN KEY(folder_id) REFERENCES Folders(folder_id)
    );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Vulnerabilities (
            vulnerability_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            severity TEXT NOT NULL,
            description TEXT NOT NULL,
            impact TEXT NOT NULL,
            solution TEXT NOT NULL,
            see_also TEXT NOT NULL,
            vuln_family TEXT NOT NULL,
            cvss_score REAL NOT NULL,
            cve_id TEXT UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Scan_Results (
            result_id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_id INTEGER,
            vulnerability_id INTEGER,
            url_id INTEGER NOT NULL,
            output INTEGER NOT NULL,
            count INTEGER NOT NULL,
            discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (scan_id) REFERENCES Scans(scan_id),
            FOREIGN KEY (url_id) REFERENCES URLs(url_id),
            FOREIGN KEY (vulnerability_id) REFERENCES Vulnerabilities(vulnerability_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Reports (
            report_id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_id INTEGER,
            report_type TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            file_path TEXT NOT NULL,
            FOREIGN KEY (scan_id) REFERENCES Scans(scan_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User_Settings (
            setting_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            setting_key TEXT NOT NULL,
            setting_value TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Notifications (
            notification_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            message TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS URLs (
            url_id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_id INTEGER,
            url TEXT NOT NULL,
            FOREIGN KEY (scan_id) REFERENCES Scans(scan_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Forms (
            form_id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_id INTEGER,
            url_id INTEGER,
            form_data TEXT NOT NULL,
            FOREIGN KEY (scan_id) REFERENCES Scans(scan_id),
            FOREIGN KEY (url_id) REFERENCES URLs(url_id)
        )
    ''')

    connection.commit()
    connection.close()

def clear_all_data():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    tables = [
        'Users',
        'Scans',
        'Vulnerabilities',
        'Scan_Results',
        'Reports',
        'User_Settings',
        'Notifications',
        'URLs',
        'Forms'
    ]
    
    for table in tables:
        cursor.execute(f'DELETE FROM {table}')
    
    connection.commit()
    connection.close()

def clear_urls_and_forms():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    tables = [
        'URLs',
        'Forms'
    ]
    
    for table in tables:
        cursor.execute(f'DELETE FROM {table}')
    
    connection.commit()
    connection.close()

def clear_scan_results():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    tables = [
        'Scan_Results'
    ]
    
    for table in tables:
        cursor.execute(f'DELETE FROM {table}')
    
    connection.commit()
    connection.close()

def clear_vulnerabilitys():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    tables = [
        'Vulnerabilities'
    ]
    
    for table in tables:
        cursor.execute(f'DELETE FROM {table}')
    
    connection.commit()
    connection.close()

def insert_user(username, password_hash, email, role):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO Users (username, password_hash, email, role)
        VALUES (?, ?, ?, ?)
    ''', (username, password_hash, email, role))

    connection.commit()
    connection.close()

def update_user(user_id, **kwargs):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    updates = ', '.join([f"{key} = ?" for key in kwargs])
    values = list(kwargs.values()) + [user_id]

    cursor.execute(f'''
        UPDATE Users
        SET {updates}, updated_at = CURRENT_TIMESTAMP
        WHERE user_id = ?
    ''', values)

    connection.commit()
    connection.close()

def delete_user(user_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        DELETE FROM Users
        WHERE user_id = ?
    ''', (user_id,))

    connection.commit()
    connection.close()

def get_user(user_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM Users
        WHERE user_id = ?
    ''', (user_id,))

    user = cursor.fetchone()
    connection.close()
    return user

def insert_scan(scan_name, user_id, description, folder_id,target_ip, status, scan_type):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO Scans (scan_name, user_id, description, folder_id, target_ip, status, scan_type)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (scan_name, user_id, description, folder_id, target_ip, status, scan_type))

    connection.commit()
    connection.close()

def insert_vulnerability(name, severity, description, impact, solution, see_also, vuln_family, cvss_score, cve_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO Vulnerabilities (name, severity, description, impact, solution, see_also, vuln_family, cvss_score, cve_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, severity, description, impact, solution, see_also, vuln_family, cvss_score, cve_id))

    connection.commit()
    connection.close()

def update_vulnerability(vulnerability_id, **kwargs):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    updates = ', '.join([f"{key} = ?" for key in kwargs])
    values = list(kwargs.values()) + [vulnerability_id]

    cursor.execute(f'''
        UPDATE Vulnerabilities
        SET {updates}
        WHERE vulnerability_id = ?
    ''', values)

    connection.commit()
    connection.close()

def delete_vulnerability(vulnerability_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        DELETE FROM Vulnerabilities
        WHERE vulnerability_id = ?
    ''', (vulnerability_id,))

    connection.commit()
    connection.close()

def insert_scan_result(scan_id, vulnerability_id, url_id, count, output):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    

    cursor.execute('''
        INSERT INTO Scan_Results (scan_id, vulnerability_id, url_id, count, output)
        VALUES (?, ?, ?, ?, ?)
    ''', (scan_id, vulnerability_id, url_id, count, output))

    connection.commit()
    connection.close()


def update_scan_result(result_id, **kwargs):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    updates = ', '.join([f"{key} = ?" for key in kwargs])
    values = list(kwargs.values()) + [result_id]

    cursor.execute(f'''
        UPDATE Scan_Results
        SET {updates}
        WHERE result_id = ?
    ''', values)

    connection.commit()
    connection.close()


def delete_scan_result(result_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        DELETE FROM Scan_Results
        WHERE result_id = ?
    ''', (result_id,))

    connection.commit()
    connection.close()


def insert_report(scan_id, report_type, file_path):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO Reports (scan_id, report_type, file_path)
        VALUES (?, ?, ?)
    ''', (scan_id, report_type, file_path))

    connection.commit()
    connection.close()


def update_report(report_id, **kwargs):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    updates = ', '.join([f"{key} = ?" for key in kwargs])
    values = list(kwargs.values()) + [report_id]

    cursor.execute(f'''
        UPDATE Reports
        SET {updates}
        WHERE report_id = ?
    ''', values)

    connection.commit()
    connection.close()

def delete_report(report_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        DELETE FROM Reports
        WHERE report_id = ?
    ''', (report_id,))

    connection.commit()
    connection.close()


def insert_user_setting(user_id, setting_key, setting_value):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO User_Settings (user_id, setting_key, setting_value)
        VALUES (?, ?, ?)
    ''', (user_id, setting_key, setting_value))

    connection.commit()
    connection.close()


def update_user_setting(setting_id, **kwargs):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    updates = ', '.join([f"{key} = ?" for key in kwargs])
    values = list(kwargs.values()) + [setting_id]

    cursor.execute(f'''
        UPDATE User_Settings
        SET {updates}
        WHERE setting_id = ?
    ''', values)

    connection.commit()
    connection.close()


def delete_user_setting(setting_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        DELETE FROM User_Settings
        WHERE setting_id = ?
    ''', (setting_id,))

    connection.commit()
    connection.close()

def get_user_setting(user_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM User_Settings
        WHERE user_id = ?
    ''', (user_id,))

    setting_data = cursor.fetchone()
    connection.close()
    return setting_data



def insert_notification(user_id, message, status):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO Notifications (user_id, message, status)
        VALUES (?, ?, ?)
    ''', (user_id, message, status))

    connection.commit()
    connection.close()


def update_notification(notification_id, **kwargs):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    updates = ', '.join([f"{key} = ?" for key in kwargs])
    values = list(kwargs.values()) + [notification_id]

    cursor.execute(f'''
        UPDATE Notifications
        SET {updates}
        WHERE notification_id = ?
    ''', values)

    connection.commit()
    connection.close()


def delete_notification(notification_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        DELETE FROM Notifications
        WHERE notification_id = ?
    ''', (notification_id,))

    connection.commit()
    connection.close()

def insert_url(scan_id, url):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO URLs (scan_id, url)
        VALUES (?, ?)
    ''', (scan_id, url))

    connection.commit()
    connection.close()


def insert_form(scan_id, url_id, form_data):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO Forms (scan_id, url_id, form_data)
        VALUES (?, ?, ?)
    ''', (scan_id, url_id, form_data))

    connection.commit()
    connection.close()


def get_all_urls():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM URLs
    ''')

    urls = cursor.fetchall()
    connection.close()
    return urls


def get_urls_by_scan_id(scan_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM URLs
        WHERE scan_id = ?
    ''', (scan_id,))

    urls = cursor.fetchall()
    connection.close()
    return [url[2] for url in urls]


def get_forms_by_scan_id(scan_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM Forms
        WHERE scan_id = ?
    ''', (scan_id,))

    forms = cursor.fetchall()
    connection.close()
    return forms


def get_forms_by_url_id(url_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM Forms
        WHERE url_id = ?
    ''', (url_id,))

    forms = cursor.fetchall()
    connection.close()
    return forms


def get_scan_id_by_name(scan_name):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()

        cursor.execute('''
            SELECT scan_id
            FROM Scans
            WHERE scan_name = ?
        ''', (scan_name,))

        result = cursor.fetchone()

        connection.close()

        # If a result was found, return the scan_id
        if result:
            return result[0]
        else:
            return None

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None


def get_target_by_scan_name(scan_name):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT target_ip
        FROM Scans
        WHERE scan_name = ?
    ''', (scan_name,))

    result = cursor.fetchone()
    connection.close()

    if result:
        return result[0]  
    return None  


def get_url_by_url_id(url_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT url FROM URLs
        WHERE url_id = ?
    ''', (url_id,))

    url_id = cursor.fetchone()
    connection.close()

    if url_id:
        return url_id[0]
    else:
        return None

def get_url_id_by_url(url):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT url_id FROM URLs
        WHERE url = ?
    ''', (url,))
    url_id = cursor.fetchone()

    if not url_id:
        modified_url = url[:-1]
        cursor.execute('''
            SELECT url_id FROM URLs
            WHERE url = ?
        ''', (modified_url,))
        url_id = cursor.fetchone()

    connection.close()

    if url_id:
        return url_id[0]
    else:
        return None


def get_all_forms_with_url(scan_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT *
        FROM Forms WHERE scan_id = ?
    ''', (scan_id,))

    forms = cursor.fetchall()
    connection.close()

    all_forms = []
    for form in forms:
        form_id, scan_id, url_id, form_data_json = form
        form_data = json.loads(form_data_json)
        all_forms.append((form_id, scan_id, url_id, form_data))

    froms_with_id = []
    for i in all_forms: 
        if len(i[3]) > 1:
            for x in i[3]:
                # print(f'The URL Form ID : {i[0]} and the Form => ',x)
                form_tuple = (get_url_by_url_id(i[2]), x)
                froms_with_id.append(form_tuple)
        else:
            if len(i[3]) == 0:
                continue
            # print(f'The URL Form ID : {i[0]} and the Form => ',i[3])
            form_tuple = (get_url_by_url_id(i[2]), i[3][0])
            froms_with_id.append(form_tuple)

    return froms_with_id

def get_data_by_vulnerability_id(vulnerability_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    cursor.execute('''
        SELECT result_id, scan_id, vulnerability_id, url_id, output, discovered_at
        FROM Scan_Results
        WHERE vulnerability_id = ?
    ''', (vulnerability_id,))
    
    results = cursor.fetchall()
    connection.close()
    
    return results

def get_vulnerability_by_id(vulnerability_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Vulnerabilities WHERE vulnerability_id = ?
    ''', (vulnerability_id,))
    vulnerability = cursor.fetchone()
    conn.close()
    return vulnerability

def get_vulnerability_id_by_name(name):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        query = '''
        SELECT vulnerability_id FROM Vulnerabilities WHERE name = ?
        '''
        
        cursor.execute(query, (name,))
        
        row = cursor.fetchone()
        
        conn.close()
        
        return row[0] if row else None
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

def get_count_by_vulnerability_id(vulnerability_id):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        query = '''
        SELECT count FROM Scan_Results WHERE vulnerability_id = ?
        '''
        
        cursor.execute(query, (vulnerability_id,))
        
        row = cursor.fetchone()
        
        conn.close()
        
        return row[0] if row else 0
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

def update_count_for_vulnerability(vulnerability_id, new_count):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    query = '''
    UPDATE Scan_Results
    SET count = ?
    WHERE vulnerability_id = ?
    '''
    
    cursor.execute(query, (new_count, vulnerability_id))
    
    conn.commit()
    
    conn.close()


def add_vulnerabilites():
    import Forms_of_vuln as f
    y = 1

    x = f.SSL_TLS_Form()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )
    y += 1

    x = f.TRACE_TRACK_Mathod_Form()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )
    y += 1

    x = f.PHP_Unsupported_Version_Detection()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )
    y += 1

    x = f.PUT_DELETE_Mathod_Form()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )
    y += 1

    x = f.OPTIONS_Mathod_Form()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )
    y += 1

    x = f.Content_Security_Policy_Header_Missing()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )
    y += 1

    x = f.Permissions_Policy_Header_Missing()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )
    y += 1

    x = f.Referrer_Policy_Header_Missing()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )
    y += 1

    x = f.Duplicate_HTTP_Headers()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )
    y += 1

    x = f.X_XSS_Header_Missing()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )
    y += 1

    x = f.Content_Type_Header_Missing()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )
    y += 1

    x = f.Cache_Control_Header_Missing()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )
    y += 1

    x = f.X_Content_Type_Options_Header_Missing()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )
    y += 1

    x = f.X_Frame_Options_Header_Missing()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )
    y += 1

    x = f.webserver_name_Form()
    insert_vulnerability(
        f"{x[0].strip()}", 
        f"{x[1].strip()}",
        f"{x[2].strip()}",
        f"{x[3].strip()}",
        f"{x[4].strip()}",
        f"{x[5].strip()}",
        f"{x[6].strip()}",
        "Nan",
        y
        )

def get_vulnerability_ids_by_scan_id(scan_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT vulnerability_id
        FROM Scan_Results
        WHERE scan_id = ?
    ''', (scan_id,))

    vulnerability_ids = [row[0] for row in cursor.fetchall()]

    connection.close()

    return vulnerability_ids

def get_all_scan_ids():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT scan_id
        FROM Scans
    ''')

    scan_ids = [row[0] for row in cursor.fetchall()]

    connection.close()

    return scan_ids



def create_folder(folder_name, user_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Folders (folder_name, user_id)
        VALUES (?, ?)
    ''', (folder_name, user_id))
    conn.commit()
    conn.close()

def get_folders():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Folders')
    folders = cursor.fetchall()
    conn.close()
    return folders

def update_folder(folder_id, folder_name):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Folders
        SET folder_name = ?, updated_at = ?
        WHERE folder_id = ?
    ''', (folder_name, datetime.now(), folder_id))
    conn.commit()
    conn.close()

def delete_folder(folder_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Folders WHERE folder_id = ?', (folder_id,))
    conn.commit()
    conn.close()

def folder_exists(folder_name):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 1 FROM Folders WHERE folder_name = ?
    ''', (folder_name,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def check_if_scans_exist():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM Scans')
    count = cursor.fetchone()[0]
    
    conn.close()
    return count > 0


def get_folder_id_by_name(folder_name):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT folder_id FROM Folders WHERE folder_name = ?', (folder_name,))
    folder_id = cursor.fetchone()
    conn.close()
    return folder_id[0] if folder_id else None

def get_scans_by_folder_id(folder_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT *
        FROM Scans
        WHERE folder_id = ?
    ''', (folder_id,))
    scans = cursor.fetchall()
    conn.close()
    return scans

def delete_scan_by_name(scan_name):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM Scans
        WHERE scan_name = ?
    ''', (scan_name,))
    conn.commit()
    conn.close()


def delete_scans_by_folder_id(folder_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Scans WHERE folder_id = ?', (folder_id,))
    conn.commit()
    conn.close()

def get_all_scans():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Scans')
    scans = cursor.fetchall()
    conn.close()
    return scans

def get_scan_by_name(scan_name):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Scans WHERE scan_name = ?', (scan_name,))
    scan_data = cursor.fetchall()
    conn.close()
    return scan_data


def get_scan_results_by_scan_id(scan_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Scan_Results
        WHERE scan_id = ?
    ''', (scan_id,))
    results = cursor.fetchall()
    conn.close()
    return results

def get_vulnerability_by_id_1(vulnerability_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Vulnerabilities WHERE vulnerability_id = ?
    ''', (vulnerability_id,))
    
    # Fetch column names and row data before closing connection
    row = cursor.fetchone()
    columns = [description[0] for description in cursor.description]
    
    conn.close()

    if row is None:
        return None
    
    # Convert row to dictionary
    vulnerability = dict(zip(columns, row))
    
    return vulnerability


for i in get_vulnerability_by_id_1(12):
    print(i)

# clear_scan_results()

# add_vulnerabilites()


# print(get_url_id_by_url('http://testphp.vulnweb.com/'))

# for i in get_all_scans():
#     print(i)


# print(get_scan_by_name('Gaza')[0])


# print(get_scans_by_folder_id(1)[0][1])
# update_folder(4, 'Scan 4')

# insert_scan('Test', 1, 'This Scan For Test Website', '1','http://testphp.vulnweb.com', 'pending', 'full')
# insert_scan('Home', 1, 'This Scan For My Home', '2','192.168.1.1', 'pending', 'full')
# insert_scan('vulnweb', 1, 'This Scan For vulnweb', '3','http://testphp.vulnweb.com/', 'pending', 'full')
# insert_scan('caffee', 1, 'This Scan For Test Website', '1','http://testphp.vulnweb.com', 'pending', 'full')

# create_tables()

# create_folder('My Scans', 1)
# create_folder('Scan 1', 1)
# create_folder('Scan 2', 1)
# create_folder('Scan 3', 1)
# create_folder('Scan 4', 1)
# create_folder('Scan 4', 1)

# add_vulnerabilites()
# clear_vulnerabilitys()

# print(get_vulnerability_ids_by_scan_id(3))

# clear_scan_results()

# print(get_url_id_by_url('http://testphp.vulnweb.com/'))

# clear_scan_results

# print(get_vulnerability_id_by_name('TLS Version 1.0 Protocol Detection'))

# vulnerability_id = 3
# data = get_vulnerability_by_id(vulnerability_id)
# print(data)


# add_vulnerabilites()

# for i in range(85,127):
#     print(f"{i} ID: ",get_url_by_url_id(i))

# for i in get_all_forms_with_url(3):
    # print(i)

# for i in get_all_forms_with_url(3):
#     print(i)
#     print()

# insert_url(scan_id, url):

# insert_form(1,1, '<form><input name="username"></form>')

# clear_urls_and_forms()
# clear_all_data()

# print(get_scan_id_by_name('Home'))
# add_vulnerabilites()


# insert_scan('Initial Scan', 1, '192.168.1.1', 'pending', 'full')
# print(get_user(1))
# delete_user(1)
# update_user(1, username='new_admin', email='new_admin@example.com')
# insert_user('admin', 'hashed_password', 'admin@example.com', 'admin')
