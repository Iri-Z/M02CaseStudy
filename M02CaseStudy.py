# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 2023

@author: Iri Zink

Display if a student has made the Bean's list or Honor Roll based on their GPA
"""

#Get user input and explain exit condition
lName = input("Plese enter student's last name or ZZZ to exit: \n")

#if the last name is not the exit condition then ask for more details
while(lName != 'ZZZ'):
    fName = input("Plese enter the student's first name: \n")
    gpa = input("Please enter the student's GPA: \n")

    if (float(gpa) >= 3.5):
        print(fName, lName, "has made the Dean's List.")
    elif (float(gpa) >= 3.25):
        print(fName, lName, "has made the Honor Roll")
    lName = input("Plese enter next student's last name or ZZZ to exit: \n")