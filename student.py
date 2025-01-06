"""
Student Class for OOP Implementation
Purpose: Used in "matching.py" for data handling.

Created By: Haydn Stucker

Created Date: 12/18/2024
Last Modified: 1/3/2025
"""

class Student:
    def __init__(self, name, email, studentID, credit_hours, work_hours, driving, NDA, weekends, job,
        incompatible_students, grades, skills, projects): # Information that can be initialized from the Qualitrics form.
        self.name = name
        self.email = email
        self.studentID = studentID
        self.credit_hours = credit_hours
        self.work_hours = work_hours
        self.driving = driving
        self.NDA = NDA
        self.weekends = weekends
        self.job = job
        self.incompatible_students = incompatible_students # saved as a list
        self.grades = grades # saved as a dictionary
        self.skills = skills # saved as a dictionary
        self.projects = projects # saved as a dictionary
        self.adjusted_skills = {} # saved as a dictionary

    def display_contents(self):
        print("\nName: ", self.name)
        print("Email: ", self.email)
        print("Student ID: ", self.studentID)
        print("Credit Hours: ", self.credit_hours)
        print("Work Hours: ", self.work_hours)
        print("Driving: ", self.driving)
        print("NDA: ", self.NDA)
        print("Weekends: ", self.weekends)
        print("Job: ", self.job)
        print("Incompatible Students: ", self.incompatible_students)
        print("Grades: ", self.grades)
        print("Skills: ", self.skills)
        print("Projects: ", self.projects)
        print("Adjusted Skills: ", self.adjusted_skills)
        print("\n---END---\n")
    
    def adjust_skills_ratings(self):
        self.adjusted_skills = {
            "Writing": self.skills["Writing Ability"],
            "Python": (self.skills["Python"] + self.grades["ISE417"] + self.grades["ISE435"] + self.grades["ISE437"]) / 4,
            "VBA Programming": self.skills["VBA Programming"],
            "MATLAB": self.skills["MATLAB"],
            "Simulation": (self.skills["Simulation/Simio"] + self.grades["ISE441"]) / 2,
            "Production/Manufactuing Systems": (self.skills["Production/Manufacturing Systems"] + self.grades["ISE316"]) / 2,
            "Quality": (self.skills["Quality"] + self.grades["ISE443"]) / 2,
            "Material Flow/Materials": (self.skills["Material Flow/Materials"] + self.grades["ISE316"]) / 2,
            "Ergonomics": (self.skills["Ergonomics"] + self.grades["ISE352"] + self.grades["ISE452"]) / 3,
            "Supply Chain Planning": (self.skills["Supply Chain Planning"] + self.grades["ISE453"]) / 2,
            "Analytics": (self.skills["Analytics"] + self.grades["ISE361"] + self.grades["ISE362"]) / 3,
            "CAD/CAM": (self.skills["CAD/CAM"] + self.grades["ISE216"] + self.grades["ISE316"]) / 3,
            "Product Development, Prototyping and Testing": (self.skills["Product Development, Prototyping and Testing"] + self.grades["ISE216"]) / 2,
            "Business Process Modeling": self.skills["Business Process Modeling"],
            "Engineering Economic Analysis": self.skills["Engineering Economic Analysis"],
            "Layout Optimization": self.skills["Layout Optimization"],
            "Lean Six Sigma": self.skills["Lean Six Sigma"],
            "Logistics/Supply Chain": (self.skills["Logistics/Supply Chain"] + self.grades["ISE361"] + self.grades["ISE362"] + self.grades["ISE453"]) / 4,
            "Scheduling": (self.skills["Scheduling"] + self.grades["ISE408"]) / 2,
            "Motion Time Studies": (self.skills["Motion Time Studies"] + self.grades["ISE352"]) / 2
        }

    