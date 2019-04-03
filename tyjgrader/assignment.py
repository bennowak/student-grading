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

# for i in range(4, len(argv)):
#     if i % 2 == 0:
#         _eval_fields.append(argv[i])
#     else:
#         _eval_texts.append(argv[i])
#
# for i in range(0, len(_eval_fields)):
#     print(f"{_eval_fields[i]} = {_eval_texts[i]}")


def create_grades():
    data = utils.get_input()
    if data:
        _new_dir = os.path.join(data["folder"])
        _eval_dir = os.path.join(data["folder"], _sub_dirs[0])
        _submit_dir = os.path.join(data["folder"], _sub_dirs[1])
        _assignment_file = os.path.join("resources", "AssignmentCSVFiles", data["assignment"])
        _template_file = os.path.join("resources", "GradingMDFiles", data["template"])

        # Make new Assignment "parent directory"
        os.makedirs(_new_dir)
        # Create tuple of students as dict("name", "url")
        students = utils.get_students(_assignment_file)
        # Create names list
        names = [student['name'] for student in students]
        # Create Assignment grading sub-directories
        utils.create_dirs(_new_dir, _sub_dirs)
        # Create student submission folders
        # utils.create_dirs(_submit_dir, names)
        utils.create_dirs(_submit_dir, names)

        # Generate evaluation files for each student
        # utils.create_eval_files(names, _eval_dir, _template_file, _eval_fields, _eval_texts)
        utils.create_eval_files(names, _eval_dir, _template_file, data["title"], data["due_date"])
        for student in students:
            if not str(student["url"]).strip() == "null":
                print(f"{_submit_dir}/{student['name']}")
                utils.download_from_github(
                    student["url"],
                    os.path.join(_submit_dir, student['name']),
                    str(data["assignment"]).replace('.csv', ''),
                    student["name"]
                )
            else:
                pass
        return 0
    else:
        print("There was an error getting data from input")
        return 0


def update(data):
    pass
