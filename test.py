import sys
from os import path

from tyjgrader import utils, assignment

# from sys import argv
#
# name_file = argv[1]
# template_file = argv[2]
# fields = []
# replacements = []
#
# for index in range(3, len(argv)):
#     if index % 2 != 0:
#         fields.append(argv[index])
#     else:
#         replacements.append(argv[index])
#
# for i in range(0, len(fields)):
#     print(f"{fields[i]} = {replacements[i]}")

assignment.create()

# base ="https://github.com/bennowak/student-grading/tree/master"

# utils.download_from_github(base, path.join("docs", "download.zip"))