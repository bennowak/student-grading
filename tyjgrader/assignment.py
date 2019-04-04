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

# tyjgrader.assignment module

import os
from . import utils

_sub_dirs = ["Grades", "Submissions", "Instructions", "Solutions", "NO_SUBMITS"]


def get_assignments():
    csv_list = utils.get_csv_list()
    assignments = {}
    for i in range(1, len(csv_list) + 1):
        assignments.update({str(i): csv_list[i - 1]})
    return assignments


# Prompts for data and either returns a dicitonary or False if exited
def get_input():
    # Generate a dictionary for existing csv files keyed to menu numbers
    assignments = get_assignments()
    # Sentinel variables
    valid_input = False
    # Prompt for csv file selection
    while not valid_input:
        # Print selection menu
        print("Please choose from the following assignment files")
        for i in range(1, len(assignments) + 1):
            print(f"{i}.) {assignments[str(i)]}")
        print("N.) Create new assignment file")
        print("X.) Quit python script")
        # Get valid input
        selection = input("Selection : ")
        valid_input = utils.is_valid_selection(selection, len(assignments))
        if valid_input:
            if selection.isdigit():
                # Is existing assignment
                print("return assignments[str(selected_csv)]")
                print(utils.get_assignment_data(assignments[selection]))
                create_grades(utils.get_assignment_data(assignments[selection]))
                return assignments[str(selection)]
            elif ord(selection) == 78 or ord(selection) == 110:
                # Is new assignment
                print("New Assignment")
                return
            elif ord(selection) == 88 or ord(selection) == 120:
                # Exit program
                print("Quit")
                return


def create_grades(data):
    if data:
        _new_dir = os.path.join(data["folder"])
        _eval_dir = os.path.join(data["folder"], _sub_dirs[0])
        _submit_dir = os.path.join(data["folder"], _sub_dirs[1])
        _assignment_file = os.path.join("resources", "AssignmentCSVFiles", data["assignment"])
        _template_file = os.path.join("resources", "GradingMDFiles", f'{data["template"]}'.strip())

        # Make new Assignment "parent directory"
        os.makedirs(_new_dir)
        # Create tuple of students as dict("name", "url")
        students = utils.get_students(_assignment_file)
        # Create names list
        names = [student['name'] for student in students]
        # Create Assignment grading sub-directories
        utils.create_dirs(_new_dir, _sub_dirs)
        # Create student submission folders
        utils.create_dirs(_submit_dir, names)

        # Generate evaluation files for each student
        utils.create_eval_files(names, _eval_dir, _template_file, data["title"], data["due_date"], data["graded_by"])
        for student in data["students"]:
            if not str(student["url"]).strip() == "null":
                print(f"{_submit_dir}/{student['name']}")
                utils.download_from_github(
                    student["url"],
                    os.path.join(_submit_dir, student['name']),
                    f"_{str(data['assignment']).replace('.csv', '')}",
                    student["name"]
                )
            else:
                pass
        return 0
    else:
        print("There was an error getting data from input")
        return 0


def update(data):
    if data:
        _new_dir = os.path.join(data["folder"])
        _eval_dir = os.path.join(data["folder"], _sub_dirs[0])
        _submit_dir = os.path.join(data["folder"], _sub_dirs[1])
        _assignment_file = os.path.join("resources", "AssignmentCSVFiles", data["assignment"])
        _template_file = os.path.join("resources", "GradingMDFiles", f'{data["template"]}'.strip())

        for student in data["students"]:
            if not str(student["url"]).strip() == "null":
                # Student has url in csv file
                # Check if submission already present
                student_dir = student["name"].replace(' ', '_')
                if not os.path.exists(os.path.join(data["folder"], "Submissions", student_dir, f'{student_dir}{data["assignment"].repace(".csv", ".zip")}')):
                    # Student submission ZIP doesn't exit
                    print(f"{_submit_dir}/{student['name']}")
                    utils.download_from_github(
                        student["url"],
                        os.path.join(_submit_dir, student['name']),
                        f"_{str(data['assignment']).replace('.csv', '')}",
                        student["name"]
                    )
