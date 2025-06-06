# Customer Realtionship Management System
Course: Information System Management

![CRM Presentation.png](https://github.com/npkyphuong04/CRM-Project/blob/main/CRM.png)


<div align="center">
  <img src="https://img.shields.io/badge/Python-3.12.3-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML">
  <img src="https://img.shields.io/badge/JavaScript-ES2023-F7DF1E?style=for-the-badge&amp;logo=javascript&amp;logoColor=black" alt="JavaScript 1.0%"> 
  <img alt="CSS" src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&amp;logo=css3&amp;logoColor=white">
  <img alt="C" src="https://img.shields.io/badge/C-17-A8B9CC?style=for-the-badge&amp;logo=c&amp;logoColor=white">
  <img alt="Jupyter Notebook" src="https://img.shields.io/badge/Jupyter_Notebook-7.0.8-F37626?style=for-the-badge&amp;logo=jupyter&amp;logoColor=white">
</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/npkyphuong04/CRM-Project">
  </a>

<h3 align="center">Customer Relationship Management Sytem</h3>
    <a href="https://github.com/npkyphuong04" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
    <a href="https://drive.google.com/drive/u/0/folders/1OKFwzx5zvCJDjB82YcIM9so7bxlSfdWv" target="_blank"><img src="https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white" alt="Google Drive"></a>
  <p align="center">
   In the fast-paced quick-service restaurant (QSR) industry, a robust CRM system is vital for fostering customer loyalty, engagement, and revenue growth. This project designs a smart CRM for Pizza Hut, tackling issues like fragmented data, lack of personalization, and inefficient workflows. By integrating online, in-store, and third-party platform data, the system offers a unified customer view, enabling targeted marketing and predictive upselling. Following SMART objectives, it leverages machine learning and cloud technologies to ensure measurable outcomes. This transformative CRM enhances customer engagement, streamlines operations, and positions Pizza Hut for sustainable growth and improved satisfaction in the digital era.
    <br />
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
# Table of contents :round_pushpin:
1. [Introduction](#Introduction)
2. [Team Members](#Team_Members)
3. [Features](#Features)
4. [Requirements](#Requirements)
5. [Installation](#Installation)
6. [Project Structure](#Project_Structure)
7. [Usage](#Usage)
7. [Acknowledgement](#Acknowledgement)
7. [References](#References)

<!-- ABOUT THE PROJECT -->

## 1. **Introduction** <a name="Introduction"></a> 📋

<div align="center">
<img src="screenshots/Intro.gif" alt="">
</div>

<div style="text-align:justify">
Pizza Hut, a leading quick-service restaurant, struggles with fragmented customer data, inconsistent communication, and inefficient manual processes, hindering personalized engagement and loyalty. A centralized CRM system can unify data from online, in-store, and delivery platforms, enabling real-time insights into customer behavior. This allows tailored promotions, boosts repeat purchases, and enhances satisfaction. By automating processes and improving cross-department communication, the CRM streamlines operations, reduces errors, and supports data-driven decisions, keeping Pizza Hut competitive in the fast-paced QSR industry.
</div>

## 2. **Team Members** <a name="Team_Members"></a> :couplekiss_man_man:

| Order |         Name          |     ID      |              Email               |                       Github account                        |                               Roles                                | Contribution (%) |                   
| :---: |:---------------------:|:-----------:|:--------------------------------:|:----------------------------------------------------:| :----------------------------------------------------------------: |:----------------:|
|   1   |    Bành Vĩnh Thuận    | ITITIU21323 | ITITIU21323@student.hcmiu.edu.vn |  [Banh-Vinh-Thuan](https://github.com/Banh-Vinh-Thuan) | Front-end | 14.3% |
|   2   |   Bùi Phương Thanh    | ITITIU21311 | ITITIU21311@student.hcmiu.edu.vn |  [phuongthanhkkk](https://github.com/phuongthanhkkk) | Database  |14.3% |
|   3   |      Lê Đăng Khoa     | ITITIU21227 | ITITIU21227@student.hcmiu.edu.vn |  [Khoakhoa2812](https://github.com/Khoakhoa2812)  | Back-end |14.3% |
|   4   | Nguyễn Phạm Kỳ Phương | ITITIU21287 | ITITIU21287@student.hcmiu.edu.vn |  [npkyphuong04](https://github.com/npkyphuong04)| Back-end |14.3% |
|   5   |  Võ Trần Khánh Quỳnh  | ITITIU21024 | ITITIU21024@student.hcmiu.edu.vn |  [kquinn301](https://github.com/kquinn301)| Front-end |14.3% |
|   6   | Nguyễn Thụy Bảo Trâm  | ITDSIU21124 | ITDSIU21124@student.hcmiu.edu.vn |  [ntbtram2802](https://github.com/ntbtram2802)| Database |14.3% |
|   7   |    Nguyễn Minh Đạt    | ITDSIU22166 | ITDSIU22166@student.hcmiu.edu.vn |  [29Schiller](https://github.com/29Schiller)| Database |14.3% |


## 3. **Features** <a name="Features"></a> ✨
- User authentication (login, register)
- Customer records management (create, view, update, delete)
- User management for administrators (create, view, update, delete)
- Responsive design for dashboard
- Profile management


## 4. **Requirement** <a name="Requirement"></a> :dart:
Before running the project, ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)
- virtualenv (optional but recommended)

## 5. **Installation** <a name="Installation"></a> :hammer_and_wrench:

1. Clone the repository:
```bash
git clone <repository-url>
cd CRM_Application
```


2. Create a virtual environment:
```bash
python -m venv venv
```


3. Activate the virtual environment
```bash
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```
Note: If requirements.txt is missing, manually install common Django dependencies:
```bash
pip install django
```

5. Configure the database, follow these steps
```bash
pip install pymysql
```
```bash
pip install mysqlclient
```
Note: You may need to change the user="root", password="4444" in file mydb.py and Django’s settings into yours before run this command (Or you can create new connection with user="root", password="4444" in your MySQL Workbench):
```bash
python mydb.py
```

6. Run database migrations
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

7. Create a superuser (admin), so that you can login with this superuser
```bash
python manage.py createsuperuser
```

8. Run the development server
```bash
python manage.py runserver
```

9. Access the application at http://127.0.0.1:8000/
  
## 6. **Project Structure** <a name="Project_Structure"></a> 📂
```
src/
├── Main.java
├── controller/
│   ├── SudokuGameController.java
├── view/
│   ├── WelcomeScreen.java
│   ├── GameView.java
│   ├── GameStartListener.java
│   ├── GameActionListener.java
│   ├── TimerListener.java
│   ├── EndScreen.java
│   ├── UIUtils.java
│   ├── HintDialog.java
│   ├── HintSystem.java
├── utils/
│   ├── GameModeType.java
│   ├── DifficultyLevel.java
│   ├── Point.java
│   ├── Constants.java
├── model/
│   ├── Board.java
│   ├── Puzzle.java
│   ├── Solution.java
├── generator/
│   ├── PuzzleGenerator.java
│   ├── ClassicPuzzleGenerator.java
│   ├── IcePuzzleGenerator.java
├── validator/
│   ├── SudokuValidator.java
│   ├── StandardSudokuValidator.java
├── mode/
│   ├── GameMode.java
│   ├── ClassicMode.java
│   ├── IceMode.java
├── solver/
│   ├── SudokuSolver.java

```

## 7. Usage <a name="Usage"></a> :joystick:
1. Register a new account or log in with existing credentials (admin login)
2. Navigate the dashboard to view the data visualization
3. Administrators can manage users through the admin interface
4. Users can add, edit, delete customer records and view customer details

## 8. Acknowledgement <a name="Acknowledgement"></a> :brain:
<div style="text-align:justify">
We express our sincere gratitude and appreciation to Dr. Ho Long Van for his professional guidance. His unwavering encouragement and support were instrumental in helping our team achieve its goals.

We would also like to express our sincere gratitude to the irreplaceable members of our group. Their technical expertise and collaborative spirit were essential to our progress. Beyond their willingness to share their knowledge and troubleshoot challenges, their good humor and positive attitudes made this project an enriching and enjoyable learning experience. We are grateful to have had the opportunity to work alongside such a talented and supportive team.
</div>

## 9. References <a name="References">:bookmark:
- [How Pizza Hut Drives Customer Loyalty Through Unique Data-Driven Journeys](https://emarsys.com/why-emarsys/success-stories/how-pizza-hut-drives-customer-loyalty-through-unique-data-driven-journeys)
- [Pizza Hut CRM](https://www.scribd.com/document/260683034/Pizza-Hut-Crm)
- [How Pizza Hut uses CRM to stay top of mind (and top of app orders).](https://www.linkedin.com/pulse/how-pizza-hut-uses-crm-stay-top-mind-app-orders-kjm0c/)
- [Pizza Hut Slices Customer Base with Segmentation.](https://www.destinationcrm.com/Articles/CRM-Insights/Case-Studies/Pizza-Hut-Slices-Customer-Base-with-Segmentation-93671.aspx)
  <br />
