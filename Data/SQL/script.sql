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

CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
	city VARCHAR(100),
    region VARCHAR(100)
);

-- Sales stages (Pipeline)
CREATE TABLE Sales_Stages (
    stage_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    description TEXT,
    stage_order INT
);

-- Leads (Potential customers)
CREATE TABLE Leads (
    lead_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(100),
    phone_number VARCHAR(20),
    source VARCHAR(100),  -- e.g., Web, Referral, Ads
    status VARCHAR(50),   -- e.g., New, Contacted, Qualified
    owner_user_id INT,    -- Sales rep handling the lead
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (owner_user_id) REFERENCES Users(user_id) ON DELETE SET NULL
);

-- Opportunities (Sales chances)
CREATE TABLE Opportunities (
    opportunity_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    customer_id INT,
    stage_id INT,
    amount DECIMAL(10,2),
    expected_close_date DATE,
    probability DECIMAL(5,2), -- e.g., 0.7 = 70%
    owner_user_id INT,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (stage_id) REFERENCES Sales_Stages(stage_id)
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
CREATE TABLE Leads_Campaigns (
    lead_id INT,
    campaign_id INT,
    created_at DATETIME,
    updated_at DATETIME,
    PRIMARY KEY (lead_id, campaign_id),
    FOREIGN KEY (lead_id) REFERENCES Leads(lead_id),
    FOREIGN KEY (campaign_id) REFERENCES Campaigns(campaign_id)
);

CREATE TABLE sessions (
    session_id BIGINT PRIMARY KEY,
    customer_id INT,
    session_start DATETIME,
    session_end DATETIME,
    app_version VARCHAR(50),
    device_type VARCHAR(50),       -- mobile, desktop, tablet, etc.
	traffic_source VARCHAR(100),    -- direct, social, ads, email, etc.
    city VARCHAR(100),
    region VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
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

-- Simulate Customer data from Session
INSERT INTO Customer (customer_id, name, email, phone_number, city, region)
SELECT
    session_group_id AS customer_id,
    CONCAT('User_', session_group_id) AS name,
    CONCAT('user_', session_group_id, '@fakeemail.com') AS email,
    CONCAT('09', LPAD(session_group_id, 8, '0')) AS phone_number,
    MIN(city) AS city,
    MIN(region) AS region
FROM (
    SELECT
        session_id,
        city,
        region,
        session_id % 1000 AS session_group_id
    FROM Sessions
) AS grouped_sessions
GROUP BY session_group_id;

select * from sessions;
select * from items;
select * from events;
select * from customer;
