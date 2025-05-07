CREATE DATABASE pizzahut;
USE pizzahut;

CREATE TABLE Sessions (
  SessionID BIGINT PRIMARY KEY,
  MobileBrandName VARCHAR(100),
  Source VARCHAR(100),
  AppVersion VARCHAR(50)
);

CREATE TABLE Events (
  EventID INT AUTO_INCREMENT PRIMARY KEY,
  SessionID BIGINT,
  EventDateTime DATETIME,
  EventName VARCHAR(50),
  FOREIGN KEY (SessionID) REFERENCES Sessions(SessionID)
);

CREATE TABLE Locations (
  LocationID INT AUTO_INCREMENT PRIMARY KEY,
  SessionID BIGINT,
  City VARCHAR(100),
  Region VARCHAR(100),
  FOREIGN KEY (SessionID) REFERENCES Sessions(SessionID)
);

CREATE TABLE Items (
  ItemID INT AUTO_INCREMENT PRIMARY KEY,
  EventID INT,
  ItemName VARCHAR(255),
  ItemCategory VARCHAR(100),
  FOREIGN KEY (EventID) REFERENCES Events(EventID)
);

-- Read README file before running this script
-- Script to populate the Sessions table
INSERT INTO Sessions (SessionID, MobileBrandName, Source, AppVersion)
SELECT DISTINCT SessionID, MobileBrandName, Source, AppVersion
FROM clean_data;

-- Script to populate the Events table
INSERT INTO Events (SessionID, EventDateTime, EventName)
SELECT SessionID, EventDateTime, EventName
FROM clean_data;

-- Script to populate the Locations table
INSERT INTO Locations (SessionID, City, Region)
SELECT DISTINCT SessionID, City, Region
FROM clean_data;

-- Script to populate the Items table
INSERT INTO Items (EventID, ItemName, ItemCategory)
SELECT
    e.EventID,
    cd.itemName,
    cd.itemCategory
FROM clean_data cd
INNER JOIN Events e ON cd.SessionID = e.SessionID AND cd.EventDateTime = e.EventDateTime
WHERE cd.itemName IS NOT NULL AND cd.itemCategory IS NOT NULL;

-- Remove null from Items table
SET SQL_SAFE_UPDATES = 0; -- turn off safe update
DELETE FROM Items 
WHERE ItemName="" OR ItemCategory="";
SET SQL_SAFE_UPDATES = 1; -- turn on safe update

select * from Items;
