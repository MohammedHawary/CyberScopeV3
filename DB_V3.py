import sqlite3

def create_tables():
    connection = sqlite3.connect('vulnerability_scanner.db')
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
        CREATE TABLE IF NOT EXISTS Scans (
            scan_id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_name TEXT NOT NULL,
            user_id INTEGER,
            target_ip TEXT NOT NULL,
            status TEXT NOT NULL,
            scan_type TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            started_at TIMESTAMP,
            completed_at TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Vulnerabilities (
            vulnerability_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            severity TEXT NOT NULL,
            cvss_score REAL NOT NULL,
            cve_id TEXT UNIQUE,
            solution TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Scan_Results (
            result_id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_id INTEGER,
            vulnerability_id INTEGER,
            ip_address TEXT NOT NULL,
            port INTEGER NOT NULL,
            protocol TEXT NOT NULL,
            status TEXT NOT NULL,
            discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (scan_id) REFERENCES Scans(scan_id),
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

    connection.commit()
    connection.close()

def insert_user(username, password_hash, email, role):
    connection = sqlite3.connect('vulnerability_scanner.db')
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO Users (username, password_hash, email, role)
        VALUES (?, ?, ?, ?)
    ''', (username, password_hash, email, role))

    connection.commit()
    connection.close()

def update_user(user_id, **kwargs):
    connection = sqlite3.connect('vulnerability_scanner.db')
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
    connection = sqlite3.connect('vulnerability_scanner.db')
    cursor = connection.cursor()

    cursor.execute('''
        DELETE FROM Users
        WHERE user_id = ?
    ''', (user_id,))

    connection.commit()
    connection.close()


def get_user(user_id):
    connection = sqlite3.connect('vulnerability_scanner.db')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM Users
        WHERE user_id = ?
    ''', (user_id,))

    user = cursor.fetchone()
    connection.close()
    return user


def insert_scan(scan_name, user_id, target_ip, status, scan_type):
    connection = sqlite3.connect('vulnerability_scanner.db')
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO Scans (scan_name, user_id, target_ip, status, scan_type)
        VALUES (?, ?, ?, ?, ?)
    ''', (scan_name, user_id, target_ip, status, scan_type))

    connection.commit()
    connection.close()


def insert_vulnerability(name, description, severity, cvss_score, cve_id, solution):
    connection = sqlite3.connect('vulnerability_scanner.db')
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO Vulnerabilities (name, description, severity, cvss_score, cve_id, solution)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, description, severity, cvss_score, cve_id, solution))

    connection.commit()
    connection.close()


def update_vulnerability(vulnerability_id, **kwargs):
    connection = sqlite3.connect('vulnerability_scanner.db')
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
    connection = sqlite3.connect('vulnerability_scanner.db')
    cursor = connection.cursor()

    cursor.execute('''
        DELETE FROM Vulnerabilities
        WHERE vulnerability_id = ?
    ''', (vulnerability_id,))

    connection.commit()
    connection.close()


def insert_scan_result(scan_id, vulnerability_id, ip_address, port, protocol, status):
    connection = sqlite3.connect('vulnerability_scanner.db')
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO Scan_Results (scan_id, vulnerability_id, ip_address, port, protocol, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (scan_id, vulnerability_id, ip_address, port, protocol, status))

    connection.commit()
    connection.close()


def update_scan_result(result_id, **kwargs):
    connection = sqlite3.connect('vulnerability_scanner.db')
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
    connection = sqlite3.connect('vulnerability_scanner.db')
    cursor = connection.cursor()

    cursor.execute('''
        DELETE FROM Scan_Results
        WHERE result_id = ?
    ''', (result_id,))

    connection.commit()
    connection.close()


def insert_report(scan_id, report_type, file_path):
    connection = sqlite3.connect('vulnerability_scanner.db')
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO Reports (scan_id, report_type, file_path)
        VALUES (?, ?, ?)
    ''', (scan_id, report_type, file_path))

    connection.commit()
    connection.close()


def update_report(report_id, **kwargs):
    connection = sqlite3.connect('vulnerability_scanner.db')
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
    connection = sqlite3.connect('vulnerability_scanner.db')
    cursor = connection.cursor()

    cursor.execute('''
        DELETE FROM Reports
        WHERE report_id = ?
    ''', (report_id,))

    connection.commit()
    connection.close()


def insert_user_setting(user_id, setting_key, setting_value):
    connection = sqlite3.connect('vulnerability_scanner.db')
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO User_Settings (user_id, setting_key, setting_value)
        VALUES (?, ?, ?)
    ''', (user_id, setting_key, setting_value))

    connection.commit()
    connection.close()


def update_user_setting(setting_id, **kwargs):
    connection = sqlite3.connect('vulnerability_scanner.db')
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
    connection = sqlite3.connect('vulnerability_scanner.db')
    cursor = connection.cursor()

    cursor.execute('''
        DELETE FROM User_Settings
        WHERE setting_id = ?
    ''', (setting_id,))

    connection.commit()
    connection.close()


def insert_notification(user_id, message, status):
    connection = sqlite3.connect('vulnerability_scanner.db')
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO Notifications (user_id, message, status)
        VALUES (?, ?, ?)
    ''', (user_id, message, status))

    connection.commit()
    connection.close()


def update_notification(notification_id, **kwargs):
    connection = sqlite3.connect('vulnerability_scanner.db')
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
    connection = sqlite3.connect('vulnerability_scanner.db')
    cursor = connection.cursor()

    cursor.execute('''
        DELETE FROM Notifications
        WHERE notification_id = ?
    ''', (notification_id,))

    connection.commit()
    connection.close()





# insert_scan('Initial Scan', 1, '192.168.1.1', 'pending', 'full')
# print(get_user(1))
# delete_user(1)
# update_user(1, username='new_admin', email='new_admin@example.com')
# insert_user('admin', 'hashed_password', 'admin@example.com', 'admin')
create_tables()