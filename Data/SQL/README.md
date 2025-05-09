Data Import using MySQL Workbench Wizard:
1. Right-click on the pizzahut database (in Navigator Pane)
2. Select "Table Data Import Wizard".
3. Click "Browse..." and find the clean_data.csv file in your cloned project. Click "Open" -> "Next"
4. In Select Destination:
    - Click "Create new table" 
    - Click "Next"
5. In "Configure Import Settings":
    - Click the Wrench icon to check:
        + Field Separator: ,
        + Enclose Strings:  " 
    - Encoding: utf-8
    - Column :
         SessionID: bigint
         EventDateTime, SessionStart,SessionEnd: datetime
    - Click "Next"
6. Click "Next" to start the import.
7. Click "Finish" when done.
8. Verify the data in the clean_data table.

Table description:
1. Core Tables
•	Users: Stores system user information (web user). 
•	Customers: Stores information about customers.
2. Sales Management Tables
•	Leads: Store information about potential customers. 
•	Opportunities: Stores infor of sales opportunities. 
•	Sales_Stages: Stores the stages of the sales process.
3.  Marketing Tables
•	Campaigns: Stores infor of marketing campaigns. 
•	Leads_Campaigns: Connects potential customers with marketing campaigns. 
