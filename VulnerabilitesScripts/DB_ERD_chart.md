Tables and Relationships

1. Users

. user_id: INTEGER, Primary Key, Auto-increment
. username: TEXT, Unique, Not Null
. password_hash: TEXT, Not Null
. email: TEXT, Unique, Not Null
. role: TEXT, Not Null
. created_at: TIMESTAMP, Default Current Timestamp
. updated_at: TIMESTAMP, Default Current Timestamp 

---

2. Scans

. scan_id: INTEGER, Primary Key, Auto-increment
. scan_name: TEXT, Not Null
. user_id: INTEGER, Foreign Key (References Users(user_id))
. description: TEXT, Not Null
. folder_name: TEXT, Not Null
. target_ip: TEXT, Not Null
. status: TEXT, Not Null
. scan_type: TEXT, Not Null
. created_at: TIMESTAMP, Default Current Timestamp
. started_at: TIMESTAMP
. completed_at: TIMESTAMP

---

3. Vulnerabilities

. vulnerability_id: INTEGER, Primary Key, Auto-increment
. name: TEXT, Not Null
. severity: TEXT, Not Null
. description: TEXT, Not Null
. impact: TEXT, Not Null
. solution: TEXT, Not Null
. see_also: TEXT, Not Null
. cvss_score: REAL, Not Null
. cve_id: TEXT, Unique

---

4. Scan_Results

. result_id: INTEGER, Primary Key, Auto-increment
. scan_id: INTEGER, Foreign Key (References Scans(scan_id))
. vulnerability_id: INTEGER, Foreign Key (References Vulnerabilities(vulnerability_id))
. ip_address: TEXT, Not Null
. port: INTEGER, Not Null
. protocol: TEXT, Not Null
. status: TEXT, Not Null
. discovered_at: TIMESTAMP, Default Current Timestamp

---

5. Reports

.report_id: INTEGER, Primary Key, Auto-increment
.scan_id: INTEGER, Foreign Key (References Scans(scan_id))
.report_type: TEXT, Not Null
.created_at: TIMESTAMP, Default Current Timestamp
.file_path: TEXT, Not Null

---

6. User_Settings

. setting_id: INTEGER, Primary Key, Auto-increment
. user_id: INTEGER, Foreign Key (References Users(user_id))
. setting_key: TEXT, Not Null
. setting_value: TEXT, Not Null

---

7. Notifications

. notification_id: INTEGER, Primary Key, Auto-increment
. user_id: INTEGER, Foreign Key (References Users(user_id))
. message: TEXT, Not Null
. status: TEXT, Not Null
. created_at: TIMESTAMP, Default Current Timestamp

---

8. URLs

. url_id: INTEGER, Primary Key, Auto-increment
. scan_id: INTEGER, Foreign Key (References Scans(scan_id))
. url: TEXT, Not Null

---

9. Forms

. form_id: INTEGER, Primary Key, Auto-increment
. scan_id: INTEGER, Foreign Key (References Scans(scan_id))
. url_id: INTEGER, Foreign Key (References URLs(url_id))
. form_data: TEXT, Not Null

---

[Users]
| user_id (PK)
| username (UN)
| password_hash
| email (UN)
| role
| created_at
| updated_at

[Scans]
| scan_id (PK)
| scan_name
| user_id (FK)
| description
| folder_name
| target_ip
| status
| scan_type
| created_at
| started_at
| completed_at

[Vulnerabilities]
| vulnerability_id (PK)
| name
| severity
| description
| impact
| solution
| see_also
| cvss_score
| cve_id (UN)

[Scan_Results]
| result_id (PK)
| scan_id (FK)
| vulnerability_id (FK)
| ip_address
| port
| protocol
| status
| discovered_at

[Reports]
| report_id (PK)
| scan_id (FK)
| report_type
| created_at
| file_path

[User_Settings]
| setting_id (PK)
| user_id (FK)
| setting_key
| setting_value

[Notifications]
| notification_id (PK)
| user_id (FK)
| message
| status
| created_at

[URLs]
| url_id (PK)
| scan_id (FK)
| url

[Forms]
| form_id (PK)
| scan_id (FK)
| url_id (FK)
| form_data

Relationships

1. Users to Scans: One-to-Many (one user can create many scans)
2. Scans to Scan_Results: One-to-Many (one scan can have many results)
3. Scans to Reports: One-to-Many (one scan can generate many reports)
4. Scans to URLs: One-to-Many (one scan can have many URLs)
5. URLs to Forms: One-to-Many (one URL can have many forms)
6. Vulnerabilities to Scan_Results: One-to-Many (one vulnerability can appear in many scan results)
7. Users to User_Settings: One-to-Many (one user can have many settings)
8. Users to Notifications: One-to-Many (one user can have many notifications)
