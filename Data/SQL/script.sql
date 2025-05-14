CREATE DATABASE pizzahut;
USE pizzahut;

-- Stores system user information ( web user)
CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL, -- Should store hashed passwords
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    role VARCHAR(50) DEFAULT 'user',
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Contacts (
    contact_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    city VARCHAR(100),
    region VARCHAR(100),
    status VARCHAR(50),          -- 'Lead', 'Customer'
    owner_user_id INT,
    FOREIGN KEY (owner_user_id) REFERENCES Users(user_id)
);

-- Marketing campaigns
CREATE TABLE Campaigns (
    campaign_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    type VARCHAR(50),
    status VARCHAR(50),
    start_date DATE,
    end_date DATE,
    budget DECIMAL(10,2),
    created_at DATETIME,
    updated_at DATETIME
);

-- Mapping leads ↔ campaigns
CREATE TABLE Contact_Campaigns (
	contact_id INT,
    campaign_id INT,
    created_at DATETIME,
    updated_at DATETIME,
    PRIMARY KEY (contact_id, campaign_id),
    FOREIGN KEY (contact_id) REFERENCES Contacts(contact_id),
    FOREIGN KEY (campaign_id) REFERENCES Campaigns(campaign_id)
);

CREATE TABLE sessions (
    session_id BIGINT PRIMARY KEY,
	contact_id INT,
    session_start DATETIME,
    session_end DATETIME,
    app_version VARCHAR(50),
    device_type VARCHAR(50),       -- mobile, desktop, tablet, etc.
	traffic_source VARCHAR(100),    -- direct, social, ads, email, etc.
    city VARCHAR(100),
    region VARCHAR(50),
    FOREIGN KEY (contact_id) REFERENCES Contacts(contact_id)
);

CREATE TABLE items (
    item_id INT PRIMARY KEY,
    item_category VARCHAR(100),  
    item_name VARCHAR(255)
);

CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id BIGINT,
    event_time DATETIME,
    event_name VARCHAR(50), 
    item_id INT,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

-- Read README file before running this script
-- Script to populate the Sessions table
INSERT INTO sessions (session_id, app_version, city, region, device_type, traffic_source, session_start, session_end)
SELECT 
    SessionID,
    MAX(AppVersion),
    MAX(City),
    MAX(Region),
    MAX(MobileBrandName),
    MAX(Source),
    MIN(EventDateTime),
    MAX(EventDateTime)
FROM clean_data
WHERE SessionID IS NOT NULL
GROUP BY SessionID;

-- Script to populate the Items table
INSERT INTO items (item_id, item_category, item_name)
SELECT DISTINCT ItemID, ItemCategory, ItemName
FROM clean_data
WHERE ItemId IS NOT NULL;

-- Script to populate the Events table
INSERT INTO events (session_id, event_time, event_name, item_id)
SELECT SessionID, EventDateTime, EventName, ItemID
FROM clean_data;

-- Simulate contact data from Session
INSERT INTO Contacts (contact_id, name, email, phone_number, city, region, status)
SELECT
    session_group_id AS customer_id,
    CONCAT('User_', session_group_id) AS name,
    CONCAT('user_', session_group_id, '@fakeemail.com') AS email,
    CONCAT('09', LPAD(MIN(phone_component), 8, '0')) AS phone_number,
    MIN(city) AS city,
    MIN(region) AS region,
    CASE 
        WHEN SUM(CASE WHEN event_name = 'purchase' THEN 1 ELSE 0 END) > 0 THEN 'Customer'
        ELSE 'Lead'
    END AS status
FROM (
    SELECT
        s.session_id,
        s.city,
        s.region,
        s.session_id % 100 AS session_group_id,
        s.session_id % 1000000000 AS phone_component, 
        e.event_name
    FROM Sessions s
    JOIN Events e ON s.session_id = e.session_id
) AS session_events
GROUP BY session_group_id;

-- update contact_id in session table
SET SQL_SAFE_UPDATES = 0;
UPDATE Sessions s
JOIN Contacts c ON s.session_id % 100 = c.contact_id
SET s.contact_id = c.contact_id;
SET SQL_SAFE_UPDATES = 1;

select * from sessions;
select * from items;
select * from events;
select * from contacts;
