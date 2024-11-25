I am writing to share the details of a Python-based project I have been working on. The project
is a GUI application for managing person information with Create, Read, Update, and Delete
(CRUD) functionality. Below is an overview of the project, including its features, setup
instructions, and technical details.

Project Overview
The Person Information CRUD application allows users to manage records of individuals,
including their name (in both Myanmar and English), age, gender, date of birth, and NRC
number. The application provides a graphical user interface (GUI) to perform CRUD operations
and can export the data to a Microsoft Excel file.

Key Features
Add New Person: Add new person records to the database.
Update Person: Update existing person records.
Delete Person: Delete person records from the database.
View All Records: Display all person records in a tabular format.
Export to Excel: Export all person information to a Microsoft Excel file with the click of a button.

Technologies Used
Programming Language: Python
GUI Library: Tkinter
Database: MySQL (using XAMPP for local development)
Data Export: pandas library

Setup Instructions
Prerequisites
XAMPP Installation:
Download and install XAMPP from the official XAMPP website.
Start the Apache and MySQL modules from the XAMPP Control Panel.

Python and Required Libraries:
Ensure you have Python installed on your machine. You can download it from the official Python
website.
Install necessary Python libraries using the following commands
pip install mysql-connector-python pandas

Database Configuration
Open phpMyAdmin by navigating to http://localhost/phpmyadmin in your web browser.
Create a new database named person_db.
Running the Application
Save the following Python script as person_crud_app.py:
2. Run the script using the command:
python person_crud_app.py
3. The GUI application will launch, allowing you to manage person information through the
interface.
