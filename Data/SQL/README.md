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
    - Column : Ensure column types are correct
    - Click "Next"
6. Click "Next" to start the import.
7. Click "Finish" when done.
8. Verify the data in the clean_data table.