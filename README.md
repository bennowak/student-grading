# student-grading
**A python module to simplify student grading from GitHub submissions**

## Overview
The program takes a `csv` file containing assignment data, student names, and urls for assignment submissions on GitHub, then automates the process of creating directories and grading sheets for their submissions.

## Process Description
The script will search the `resources/AssignmentCSVFiles` directory for existing assignment files.  These will show up in the main running menu.  The first row of the selected `assignment.csv` file will be parsed for assignment data used to generate a specific directory structure under the `Gradings` directory. The subsequent rows contain student names, and submission URLs for processing and downloading assignments automatically.


### "Parts" of the Process

- #### run_tyjgrader.py
    This is the main entry point for the application.  Run the script as follows:

    ```python
    python run_tyjgrader.py
    ```
- #### ./tyjgrader/ (module)
    This is the directory that contains the python processing module code
   
- #### ./TEMPLATES/
    A directory of example files as the `assignment.csv`, and `grade_sheet.md` files should be laid out
    
- #### ./resources/
    Contains directories for the actual `assignment.csv` and `grade_sheete.md` files.
    
    - #### AssignmentCSVFiles/
        The directory for individual "assignment" `csv` data files.  These are the files that will be used to process particular assignments.  
        **NOTE: BE SURE TO FORMAT THESE CORRECTLY IF NOT AUTOGENERATING THEM**      
        See the `TEMPLATE_Assignment.csv` file in the `TEMPLATES` folder for clarification

    - #### GradingMDFiles/
        The directory for individual "grading sheet" `Markdown` files. These are the files that will be used to generate individual student grade sheets for particular assignments     
        **NOTE: BE SURE TO FORMAT THESE CORRECTLY IF NOT AUTOGENERATING THEM**      
        See the `TEMPLATE_GradeSheet.md` file in the `TEMPLATES` folder for clarification

- #### ./Gradings/
    This is where the directories that are created for grading assignments will be output.
    
### Output

Given the following assignment `csv` file : 
```csv
HW00_TestGrade, Test 00, "Saturday, January 1st, 2001 at 11:59 pm", test_gradesheet.md, TA Tester
Bee Gud, https://github.com/bennowak/student-grading
Som Purrsen, null
Jam Out, https://github.com/bennowak/student-grading/archive/master.zip
```

Running the script at the command line will yield the following structure : 

![The Output](docs/Output.png)

## Folder Organization Concerns

This program is intended to reside inside a single directory where the grader (TA, Instructor, etc.) does all of their grading.  This will mean that each call to the program should supply different arguments for different assignments.  Rerunning the script with the same arguments may either overwrite previously existent files or simply fail to execute part of the script.  So what does this look like as originally intended by the author.

    - `Grading` (folder)
        - Homework01_Some_Homework
        - Homework02_Some_more_homework
        - Resources
            - hw1_students.csv
            - hw2_students.csv
            - hw1_gradingTemplate.md
            - hw2_gradingTemplate.md
            - GRADING_TEMPLATE.md
        - `tyjgrader` (module folder)

Before running the script: 
- a copy of the GRADING_TEMPLATE.md file has been customized to reflect the rubric and grading concerns for that particular assignment
- a separate `csv` for each assignment has been created containing valid URLs pointing to the GitHub `master` branch for the relevant student's submission
- arguments to the program have been entered meticulously and accurately

## If An Error Occurs

- Delete the folder for that assignment and try again and check the formatting of your csv and arguments to the `run_tyjgrader.py` script.

- Report issues here [here](https://github.com/bennowak/student-grading/issues)


```
    TYJ Student Grading
    Copyright (C) 2019  Benjamin Nowak

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see http://www.gnu.org/licenses/.
```