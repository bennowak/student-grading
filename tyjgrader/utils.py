   # TYJ Student Grading
   #  Copyright (C) 2019  Benjamin Nowak
   #
   #  This program is free software: you can redistribute it and/or modify
   #  it under the terms of the GNU Affero General Public License as
   #  published by the Free Software Foundation, either version 3 of the
   #  License, or (at your option) any later version.
   #
   #  This program is distributed in the hope that it will be useful,
   #  but WITHOUT ANY WARRANTY; without even the implied warranty of
   #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   #  GNU Affero General Public License for more details.
   #
   #  You should have received a copy of the GNU Affero General Public License
   #  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# tyjgrader.utils module
import os
from urllib import request
import csv


def get_assignment_data(assignment):
    if assignment:
        with open(os.path.join("resources", "AssignmentCSVFiles", assignment)) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            # Get first line which is assignment info
            info = next(csv_reader)
            students = []
            # correct number of values is 4
            if len(info) == 5:
                for student in csv_reader:
                    students.append({"name": student[0], "url": student[1]})
                assignment = {
                    "folder": info[0],
                    "assignment": assignment,
                    "title": info[1],
                    "due_date": info[2],
                    "template": info[3],
                    "graded_by": info[4].strip(),
                    "students": students
                }
                return assignment
            else:
                print("Error: Incorrectly formatted assignment csv file")
                return False
    else:
        print("Error: assignment argument invalid in get_assignment_data")
        return False

def get_names(students_csv):
    names = []
    with open(students_csv) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for student in csv_reader:
            names.append(student[0].strip('\n'))
    return tuple(names)


def get_students(students_csv):
    names = []

    with open(students_csv) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        # Skip the first line which is title, date, and graded_by
        next(csv_reader)
        for student in csv_reader:
            names.append({"name": student[0], "url": student[1]})
    return tuple(names)


def create_dirs(parent_dir, names):
    if os.path.exists(parent_dir):
        for name in names:
            os.makedirs(parent_dir + "/" + name.replace(' ', '_'))


def create_eval_files(names, eval_dir, path_to_eval_template, assignment, due_date, graded_by):
    if os.path.exists(eval_dir):
        with open(path_to_eval_template) as template:
            content = template.readlines()
        for name in names:
            eval_file = open(f"{eval_dir}/" + name.replace(' ', '_') + ".md", 'w', 1)
            for line in content:
                if "<name>" in line:
                    newline = line.replace("<name>", name.replace('_', ' '))
                    eval_file.writelines(newline)
                elif "<assignment>" in line:
                    newline = line.replace("<assignment>", assignment)
                    eval_file.writelines(newline)
                elif "<due>" in line:
                    newline = line.replace("<due>", due_date)
                    eval_file.writelines(newline)
                elif "<graded_by>" in line:
                    newline = line.replace("<graded_by>", graded_by)
                    eval_file.writelines(newline)
                else:
                    eval_file.writelines(line)
            eval_file.close()


def extract_base_url(url):
    parts = url.split('/')
    return f"{parts[0]}//{parts[2]}/{parts[3]}/{parts[4]}"


def download_from_github(url, save_dir, assignment, student):
    zip_master = f"{extract_base_url(url)}/archive/master.zip"
    data = request.urlopen(zip_master)
    filename = f"{save_dir}/{student}{assignment}.zip"
    f = open(filename.replace(' ', '_'), 'wb')
    f.write(data.read())
    f.close()


def new_assignment(file_name, title, due_date, graded_by):
    _res_path = os.path.join("resources", "AssignmentCSVFiles")
    print(os.listdir(_res_path))
    if f"{file_name}1.csv" in os.listdir(_res_path):
        print("ERROR: A csv file with that name already exists!")
        return False
    else:
        with open(os.path.join("resources", "students.txt")) as students:
            names = students.readlines()
        assignment_file = open(os.path.join(_res_path, f"{file_name}.csv"), 'w', 1)
        assignment_file.writelines(f"{title}, {due_date}, {graded_by}\n")
        for name in names:
            assignment_file.write(f"{name.strip()}, null\n")
        assignment_file.close()



def is_valid_selection(selection, choice_count):
    if len(selection) == 1:
        if selection.isdigit() and 0 < int(selection) <= choice_count:
            return True
        elif ord(selection) == 88 or ord(selection) == 120 or ord(selection) == 78 or ord(selection) == 110:
            return True
    return False


def get_csv_list():
    assignment_csv_files = os.listdir(os.path.join('.', 'resources', 'AssignmentCSVFiles'))
    return assignment_csv_files


def get_template_list():
    grading_templates = os.listdir(os.path.join('.', 'resources', 'GradingMDFiles'))
    return grading_templates


# # Prompts for data and either returns a dicitonary or False if exited
# def get_input():
#     # Generate a dictionary for csv and md files available
#     csv_list = get_csv_list()
#     temp_list = get_template_list()
#     assignments = {}
#     for i in range(1, len(csv_list) + 1):
#         assignments.update({str(i): csv_list[i - 1]})
#     templates = {}
#     for i in range(1, len(temp_list) + 1):
#         templates.update({str(i): temp_list[i - 1]})
#
#     # Sentinel variables
#     valid_csv = False
#     valid_temp = False
#     selected_csv = -1
#     selected_temp = -1
#
#     # Prompt for csv file selection
#     while not valid_csv:
#         # Print selection menu
#         print("Please choose from the following assignment files")
#         for i in range(1, len(assignments) + 1):
#             print(f"{i}.) {assignments[str(i)]}")
#         print("Enter X to quit")
#         # Get valid input
#         selection = validate_input(input("Selection : "), len(assignments))
#         # If input is within valid range set selected_csv variable and exit while loop
#         if selection >= 0:
#             valid_csv = True
#             selected_csv = selection
#     # If not exiting the program
#     if selected_csv > 0:
#         # Prompt for template file selection
#         while not valid_temp:
#             # Print selection menu
#             print("Please choose from the following grading templates")
#             for i in range(1, len(templates) + 1):
#                 print(f"{i}.) {templates[str(i)]}")
#             print("Enter X to quit")
#             # Get valid input
#             selection = validate_input(input("Selection : "), len(templates))
#             # If input is within valid range set selected_temp variable and exit while loop
#             if selection >= 0:
#                 valid_temp = True
#                 selected_temp = selection
#         # Prompt for other data
#         # title = input("What is the TITLE for the assignment? (Readable title for grade sheet, etc.")
#         # due_date = input("What is the DUE DATE for the assignment? (Readable date)")
#         folder_name = input("Please enter name for the folder. (NO SPACES, use underscore `_`").replace(' ', '_')
#         # Return a dict with data values
#         #return {"assignment": assignments[str(selected_csv)], "template": templates[str(selected_temp)]}
#         return {"assignment": assignments[str(selected_csv)]}
#     # Exit chosen; return false
#     return False
