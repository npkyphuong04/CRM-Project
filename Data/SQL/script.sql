CREATE DATABASE pizzahut;
USE pizzahut;


CREATE TABLE sessions (
    session_id BIGINT PRIMARY KEY,
    session_start DATETIME,
    session_end DATETIME,
    app_version VARCHAR(50),
    device_type VARCHAR(50),       -- mobile, desktop, tablet, etc.
	traffic_source VARCHAR(100),    -- direct, social, ads, email, etc.
    city VARCHAR(100),
    region VARCHAR(50)
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

select * from sessions;
select * from items;
select * from events;
