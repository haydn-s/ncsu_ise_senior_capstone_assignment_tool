"""
Matching Algorithm OOP Implementation
Purpose: Used to generate a list of student to company matches for ISE Capstone projects.

Created By: Haydn Stucker

Created Date: 12/18/2024
Last Modified: 1/2/2025
"""

# Import all necessary Libraries
import pandas as pd
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Import Object Dependencies
from company import Company
from student import Student

# Prompt the User to select the Companies File
print("Please select the Companies Excel file:")
CompaniesFilePath = askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])

# Prompt the User to select the Students File
print("Please select the Students Excel file:")
StudentsFilePath = askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])

# Define Global Constants
SheetName = "Sheet0"
company_objects = []
student_objects = []

# Read the Excel Files into DataFrames
companies_df = pd.read_excel(CompaniesFilePath, sheet_name = SheetName, header = None, skiprows = 2)
students_df = pd.read_excel(StudentsFilePath, sheet_name = SheetName, header = None, skiprows = 2)

# Read all Excel Data into Objects
for index, row in companies_df.iterrows(): # Creating Company Objects and adding them to the appropriate List
    company_rank_dict = {
            "Python": row[23] / 100,
            "VBA": row[24] / 100 ,
            "MATLAB": row[25] / 100 ,
            "Simulation": row[26] / 100 ,
            "Production/Manufacturing Systems": row[27] / 100 ,
            "Quality": row[28] / 100 ,
            "Material Flow / Materials": row[29] / 100 ,
            "Ergonomics": row[30] / 100 ,
            "Supply Chain Planning": row[31] / 100 ,
            "Analytics": row[32] / 100 ,
            "CAD/CAM": row[33] / 100 ,
            "Product Development, Prototyping, & Testing": row[34] / 100 ,
            "Power BI": row[35] / 100 ,
            "Business Process Modeling": row[36] / 100 ,
            "Financial Modeling": row[37] / 100 ,
            "Kanban": row[38] / 100 ,
            "Layout Optimization": row[39] / 100 ,
            "Lean Six Sigma": row[40] / 100 ,
            "Logistics / Supply Chain": row[41] / 100 ,
            "Enterprise Software": row[42] / 100 ,
            "Scheduling": row[43] / 100 ,
            "Motion Time Studies": row[44] / 100 ,
        }

    new_company = Company(row[17], row[19], row[21], row[22], company_rank_dict)
    company_objects.append(new_company)
    new_company = None
    company_rank_dict = {}

for index, row in students_df.iterrows(): # Creating Student Objects and adding them to the appropriate List
    student_grades = {
        "ISE216": row[31],
        "ISE316": row[32],
        "ECE331": row[33],
        "ISE352": row[34],
        "ISE361": row[35],
        "ISE362": row[36],
        "ISE408": row[37],
        "ISE417": row[38],
        "ISE435": row[39],
        "ISE437": row[40],
        "ISE441": row[41],
        "ISE443": row[42],
        "ISE452": row[43],
        "ISE453": row[44]
    }

    student_skills = {
        "Writing Ability": row[45],
        "Python": row[46],
        "VBA Programming": row[47],
        "MATLAB": row[48],
        "Simulation/Simio": row[49],
        "Production/Manufacturing Systems": row[50],
        "Quality": row[51],
        "Material Flow/Materials": row[52],
        "Ergonomics": row[53],
        "Supply Chain Planning": row[54],
        "Analytics": row[55],
        "CAD/CAM": row[56],
        "Product Development, Prototyping and Testing": row[57],
        "Business Process Modeling": row[58],
        "Engineering Economic Analysis": row[59],
        "Layout Optimization": row[60],
        "Lean Six Sigma": row[61],
        "Logistics/Supply Chain": row[62],
        "Scheduling": row[63],
        "Motion Time Studies": row[64]
    }

    student_projects = {
        "Choice 1": row[65],
        "Choice 2": row[66],
        "Choice 3": row[67],
        "Choice 4": row[68],
        "Choice 5": row[69],
        "Choice 6": row[70],
        "Choice 7": row[71],
        "Choice 8": row[72],
        "Choice 9": row[73],
        "Choice 10": row[74],
        "Choice 11": row[75],
        "Choice 12": row[76],
        "Choice 13": row[77],
        "Choice 14": row[78]
    }

    new_student = Student(row[17], row[18], row[19], row[22], row[23], row[24], row[25], row[26], row[27],
        row[29], student_grades, student_skills, student_projects)
    student_objects.append(new_student)
    new_student = None
    student_grades = {}
    student_skills = {}
    student_projects = {}

# Initial Filters for removing Students from Incompatible Companies
for company in company_objects: # iterate through all company objects
    for student in student_objects: # iterate through all student objects
        if student.NDA == 2 and company.NDA == 1: # validate NDA willingness
            if student.weekends == 2 and company.weekends == 1: # validate weekends willingness
                company.add_incompatible_student(student) # add the validated student to the company's list

# Compute all Adjusted Skills for each Student
for student in student_objects:
    student.adjust_skills_ratings()

    # Rank all of the Students for each Company
    for company in company_objects:
        company.rank_student(student)

# Sort all the Rankings
for company in company_objects:
    company.sort_student_ranks()

    # Remove all Incompatible Students from a Company Ranking
    for student in company.incompatible_students:
        if student.name in company.sorted_ranks:
            del company.sorted_ranks[student.name]

# Assign the Students to the Projects
for student in student_objects:
    for company in company_objects:
