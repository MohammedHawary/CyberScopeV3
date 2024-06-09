-- Users
| user_id      | INTEGER   | PRIMARY KEY AUTOINCREMENT                |
| username     | TEXT      | UNIQUE NOT NULL                          |
| password_hash| TEXT      | NOT NULL                                 |
| email        | TEXT      | UNIQUE NOT NULL                          |
| role         | TEXT      | NOT NULL                                 |
| created_at   | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP                |
| updated_at   | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP                |

-- Folders
| folder_id    | INTEGER   | PRIMARY KEY AUTOINCREMENT                |
| folder_name  | TEXT      | NOT NULL                                 |
| user_id      | INTEGER   | FOREIGN KEY REFERENCES Users(user_id)    |
| created_at   | TIMESTAMP | NOT NULL DEFAULT CURRENT_TIMESTAMP       |
| updated_at   | TIMESTAMP | NOT NULL DEFAULT CURRENT_TIMESTAMP       |

-- Scans
| scan_id      | INTEGER   | PRIMARY KEY AUTOINCREMENT                |
| scan_name    | TEXT      | NOT NULL                                 |
| user_id      | INTEGER   | FOREIGN KEY REFERENCES Users(user_id)    |
| folder_id    | INTEGER   | FOREIGN KEY REFERENCES Folders(folder_id)|
| description  | TEXT      | NOT NULL                                 |
| target_ip    | TEXT      | NOT NULL                                 |
| status       | TEXT      | NOT NULL                                 |
| scan_type    | TEXT      | NOT NULL                                 |
| created_at   | TIMESTAMP | NOT NULL DEFAULT CURRENT_TIMESTAMP       |
| started_at   | TIMESTAMP |                                          |
| completed_at | TIMESTAMP |                                          |

-- Vulnerabilities
| vulnerability_id | INTEGER | PRIMARY KEY AUTOINCREMENT               |
| name             | TEXT    | NOT NULL                                |
| severity         | TEXT    | NOT NULL                                |
| description      | TEXT    | NOT NULL                                |
| impact           | TEXT    | NOT NULL                                |
| solution         | TEXT    | NOT NULL                                |
| see_also         | TEXT    | NOT NULL                                |
| vuln_family      | TEXT    | NOT NULL                                |
| cvss_score       | REAL    | NOT NULL                                |
| cve_id           | TEXT    | UNIQUE                                  |

-- Scan_Results
| result_id        | INTEGER  | PRIMARY KEY AUTOINCREMENT              |
| scan_id          | INTEGER  | FOREIGN KEY REFERENCES Scans(scan_id)  |
| vulnerability_id | INTEGER  | FOREIGN KEY REFERENCES Vulnerabilities(vulnerability_id)|
| url_id           | INTEGER  | FOREIGN KEY REFERENCES URLs(url_id)    |
| output           | INTEGER  | NOT NULL                               |
| count            | INTEGER  | NOT NULL                               |
| discovered_at    | TIMESTAMP| DEFAULT CURRENT_TIMESTAMP              |

-- Reports
| report_id        | INTEGER  | PRIMARY KEY AUTOINCREMENT              |
| scan_id          | INTEGER  | FOREIGN KEY REFERENCES Scans(scan_id)  |
| report_type      | TEXT     | NOT NULL                               |
| created_at       | TIMESTAMP| DEFAULT CURRENT_TIMESTAMP              |
| file_path        | TEXT     | NOT NULL                               |

-- User_Settings
| setting_id       | INTEGER  | PRIMARY KEY AUTOINCREMENT              |
| user_id          | INTEGER  | FOREIGN KEY REFERENCES Users(user_id)  |
| setting_key      | TEXT     | NOT NULL                               |
| setting_value    | TEXT     | NOT NULL                               |

-- Notifications
| notification_id  | INTEGER  | PRIMARY KEY AUTOINCREMENT              |
| user_id          | INTEGER  | FOREIGN KEY REFERENCES Users(user_id)  |
| message          | TEXT     | NOT NULL                               |
| status           | TEXT     | NOT NULL                               |
| created_at       | TIMESTAMP| DEFAULT CURRENT_TIMESTAMP              |

-- URLs
| url_id           | INTEGER  | PRIMARY KEY AUTOINCREMENT              |
| scan_id          | INTEGER  | FOREIGN KEY REFERENCES Scans(scan_id)  |
| url              | TEXT     | NOT NULL                               |

-- Forms
| form_id          | INTEGER  | PRIMARY KEY AUTOINCREMENT              |
| scan_id          | INTEGER  | FOREIGN KEY REFERENCES Scans(scan_id)  |
| url_id           | INTEGER  | FOREIGN KEY REFERENCES URLs(url_id)    |
| form_data        | TEXT     | NOT NULL                               |


Relationships

Users:

Users.user_id → Folders.user_id
Users.user_id → Scans.user_id
Users.user_id → User_Settings.user_id
Users.user_id → Notifications.user_id
Folders:

Folders.user_id → Users.user_id
Folders.folder_id → Scans.folder_id
Scans:

Scans.user_id → Users.user_id
Scans.folder_id → Folders.folder_id
Scans.scan_id → Scan_Results.scan_id
Scans.scan_id → Reports.scan_id
Scans.scan_id → URLs.scan_id
Scans.scan_id → Forms.scan_id
Vulnerabilities:

Vulnerabilities.vulnerability_id → Scan_Results.vulnerability_id
URLs:

URLs.scan_id → Scans.scan_id
URLs.url_id → Scan_Results.url_id
URLs.url_id → Forms.url_id
Scan_Results:

Scan_Results.scan_id → Scans.scan_id
Scan_Results.url_id → URLs.url_id
Scan_Results.vulnerability_id → Vulnerabilities.vulnerability_id
Reports:

Reports.scan_id → Scans.scan_id
User_Settings:

User_Settings.user_id → Users.user_id
Notifications:

Notifications.user_id → Users.user_id
Forms:

Forms.scan_id → Scans.scan_id
Forms.url_id → URLs.url_id
