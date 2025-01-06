"""
Company Class for OOP Implementation
Purpose: Used in "matching.py" for data handling.

Created By: Haydn Stucker

Created Date: 12/18/2024
Last Modified: 1/3/2025
"""

class Company:
    def __init__(self, name, group_size, NDA, weekends, desired_skills): # Information that can be initialized from the Qualitrics form.
        self.name = name
        self.group_size = group_size
        self.NDA = NDA
        self.weekends = weekends
        self.desired_skills = desired_skills # saved as a dictionary
        self.incompatible_students = []
        self.student_ranks = {}
        self.sorted_ranks = {}

    def display_contents(self):
        print("\nName: ", self.name)
        print("Group Size: ", self.group_size)
        print("NDA: ", self.NDA)
        print("Weekends: ", self.weekends)
        print("Desired Skills: ", self.desired_skills)
        print("Incompatible Students: ", self.incompatible_students)
        print("Student Ranks: ", self.student_ranks)
        print("Sorted Student Ranks: ", self.sorted_ranks)
        print("\n---END---\n")

    def add_incompatible_student(self, student):
        self.incompatible_students.append(student)

    def rank_student(self, student):
        total_score = 0

        for key_company in self.desired_skills:
            for key_student in student.adjusted_skills:
                if key_company == key_student:
                    total_score = total_score + (self.desired_skills[key_company] * student.adjusted_skills[key_student])
                
        self.student_ranks[student.name] = total_score

    def sort_student_ranks(self):
        self.sorted_ranks = dict(sorted(self.student_ranks.items(), key = lambda item: item[1], reverse = True))