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


def get_names(names_file):
    names = []
    with open(names_file) as f:
        for name in f.readlines():
            names.append(name.strip('\n'))
    return tuple(names)


def create_dirs(parent_dir, names):
    if os.path.exists(parent_dir):
        for name in names:
            os.makedirs(parent_dir + "/" + name)


# [<name>, <assignment>, <due>]
# [names[], title, date]
# EXAMPLE CALL -
# create_eval_files(
#       names,
#       03_Python/grades,
#       ../templates/assignment_template.md,
#       [<name>, <assignment>, <due>],
#       [names[], title, date]
#     )
def create_eval_files(names, eval_dir, path_to_eval_template, eval_fields, eval_replacements):
    if os.path.exists(eval_dir):
        with open(path_to_eval_template) as template:
            content = template.readlines()
        for name in names:
            eval_file = open(f"{eval_dir}/" + name + ".md", 'w', 1)
            for line in content:
                if eval_fields[0] in line:
                    newline = line.replace(eval_fields[0], name.replace('_', ' '))
                    eval_file.writelines(newline)
                elif eval_fields[1] in line:
                    newline = line.replace(eval_fields[1], eval_replacements[1])

                    eval_file.writelines(newline)
                elif eval_fields[2] in line:
                    newline = line.replace(eval_fields[2], eval_replacements[2])
                    eval_file.writelines(newline)
                else:
                    eval_file.writelines(line)
            eval_file.close()


def extract_base_url(url):
    parts = url.split('/')
    return f"{parts[0]}//{parts[2]}/{parts[3]}/{parts[4]}"


def download_from_github(url, save_dir):
    zip_master = f"{extract_base_url(url)}/archive/master.zip"
    data = request.urlopen(zip_master)
    f = open(save_dir, 'wb')
    f.write(data.read())
    f.close()
