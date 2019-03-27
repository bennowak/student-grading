# tyjgrader.assignment module

import os
from sys import argv
from . import utils

_new_dir = argv[1]
_sub_dirs = ["Grades", "Submissions", "Instructions", "Solutions", "NO_SUBMITS"]
_eval_dir = _new_dir + "/" + _sub_dirs[0]
_submit_dir = _new_dir + "/" + _sub_dirs[1]
_name_file = argv[2]
_template_file = argv[3]
_eval_fields = []
_eval_texts = []

for i in range(4, len(argv)):
    if i % 2 == 0:
        _eval_fields.append(argv[i])
    else:
        _eval_texts.append(argv[i])

for i in range(0, len(_eval_fields)):
    print(f"{_eval_fields[i]} = {_eval_texts[i]}")


def create():
    # Make new Assignment "parent directory"
    os.makedirs(_new_dir)
    # Extract names of students
    names = utils.get_names(_name_file)
    # Create Assignment grading sub-directories
    utils.create_dirs(_new_dir, _sub_dirs)
    # Create StudentSubmission directories
    utils.create_dirs(_submit_dir, names)
    # Generate evauation files for each student
    utils.create_eval_files(names, _eval_dir, _template_file, _eval_fields, _eval_texts)

