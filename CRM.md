# Customer Realtionship Management System
Course: Information System Management

![CRM Presentation.png](https://github.com/nguyensngoc108/Furnitech/blob/main/Furnitech%20Presentation.png)

<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


</div>

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
  <a href="https://github.com/nguyensngoc108/Furnitech">
  </a>

<h3 align="center">Customer Relationship Management Sytem</h3>

  <p align="center">
   The CRM project for Information System Management course in semester 2 (2024 - 2025), International University - VNU HCMC.
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

## 1. **Introduction** <a name="Introduction"></a> :bricks:

<div align="center">
<img src="screenshots/Intro.gif" alt="">
</div>

<div style="text-align:justify">
A comprehensive Customer Relationship Management system built with Django that allows users to manage customer records, users list, administrative tasks, and interact with responsive dashboards.
</div>

## 2. **Team Members** <a name="Team Members"></a> :couplekiss_man_man:

| Order |         Name          |     ID      |              Email               |                       Github account                        |                               Roles                                | Contribution (%) |                   
| :---: |:---------------------:|:-----------:|:--------------------------------:|:----------------------------------------------------:| :----------------------------------------------------------------: |:----------------:|
|   1   |   Bành Vĩnh Thuận     | ITITIU21323 | ITITIU21323@student.hcmiu.edu.vn |           [TracyHT](https://github.com/TracyHT)      |   **TEAM LEADER** with Model evaluation, Hyper-parameters tuning   |        25        |
|   2   |    Bùi Phương Thanh   | ITITIU21311 | ITITIU21311@student.hcmiu.edu.vn | [nguyensngoc108](https://github.com/nguyensngoc108)  |   **TEAM LEADER** with Model evaluation, Hyper-parameters tuning   |        25        |
|   3   |    Lê Đăng Khoa       | ITITIU21227 | ITITIU21227@student.hcmiu.edu.vn |       [ITITIU20215](https://github.com/ITITIU20215)  |   **TEAM LEADER** with Model evaluation, Hyper-parameters tuning   |        25        |
|   4   | Nguyễn Phạm Kỳ Phương | ITITIU21287 | ITITIU21287@student.hcmiu.edu.vn |       [npkyphuong04](https://github.com/npkyphuong04)|   **TEAM LEADER** with Model evaluation, Hyper-parameters tuning   |        25        |
|   5   | Võ Trần Khánh Quỳnh   | ITITIU21024 | ITITIU21024@student.hcmiu.edu.vn |       [npkyphuong04](https://github.com/npkyphuong04)|   **TEAM LEADER** with Model evaluation, Hyper-parameters tuning   |        25        |
|   6   | Nguyễn Thụy Bảo Trâm  | ITDSIU21124 | ITDSIU21124@student.hcmiu.edu.vn |       [npkyphuong04](https://github.com/npkyphuong04)|   **TEAM LEADER** with Model evaluation, Hyper-parameters tuning   |        25        |
|   7   | Nguyễn Minh Đạt       | ITDSIU22166 | ITDSIU22166@student.hcmiu.edu.vn |       [npkyphuong04](https://github.com/npkyphuong04)|   **TEAM LEADER** with Model evaluation, Hyper-parameters tuning   |        25        |


## 3. **Features** <a name="Features"></a> 
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
  
## 6. **Project Structure** <a name="Project Structure"></a>
```
CRM-Project-main/
├── CRM_Application/   # Main application code
├── Data/              # Data files/resources
├── ISM_Project/       # Main Django project settings
├── manage.py          # Django management script
├── mydb.py            # Database setup script (if needed)
├── virt/              # Virtual environment (optional)
└── .idea/             # IDE configuration (optional)

```



## 7. Usage <a name="Usage"></a> :joystick:
1. Register a new account or log in with existing credentials (admin login)
2. Navigate the dashboard to view the data visualization
3. Administrators can manage users through the admin interface
4. Users can add, edit, delete customer records and view customer details



## 8. Acknowledgement <a name="Acknowledgement"></a> :brain:
<div style="text-align:justify">
We express our sincere gratitude and appreciation to Assoc. Prof. Nguyen Van Sinh for his professional guidance. His unwavering encouragement and support were instrumental in helping our team achieve its goals.
We also extend our thanks to MSc. Nguyen Trung Nghia, a laboratory lecturer, whose technical assistance and good humor greatly enriched our learning experience this semester.

We would also like to express our sincere gratitude to the irreplaceable members of our group. Their technical expertise and collaborative spirit were essential to our progress. Beyond their willingness to share their knowledge and troubleshoot challenges, their good humor and positive attitudes made this project an enriching and enjoyable learning experience. We are grateful to have had the opportunity to work alongside such a talented and supportive team.
</div>
<br />

## 9. References <a name="References">:bookmark:
- [Node.js tutorial](https://www.w3schools.com/nodejs/)
- [React.js tutorial](https://www.w3schools.com/react/default.asp)
- [MongoDB tutorial](https://www.w3schools.com/nodejs/nodejs_mongodb.asp)
- [Express.js tutorial](https://www.w3schools.com/nodejs/nodejs_express.asp)
- [Mongoose tutorial](https://www.w3schools.com/nodejs/nodejs_mongodb.asp)
- [React Router tutorial](https://www.w3schools.com/react/react_router.asp)
  <br />


[contributors-shield]: https://img.shields.io/github/contributors/nguyensngoc108/Furnitech.svg?style=for-the-badge
[contributors-url]: https://github.com/nguyensngoc108/Furnitech/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nguyensngoc108/Furnitech.svg?style=for-the-badge
[forks-url]: https://github.com/nguyensngoc108/Furnitech/network/members
[stars-shield]: https://img.shields.io/github/stars/nguyensngoc108/Furnitech.svg?style=for-the-badge
[stars-url]: https://github.com/nguyensngoc108/Furnitech/stargazers
[issues-shield]: https://img.shields.io/github/issues/nguyensngoc108/Furnitech.svg?style=for-the-badge
[issues-url]: https://github.com/nguyensngoc108/Furnitech/issues
