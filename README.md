# student-grading
**A python module to simplify student grading from GitHub submissions**

## Overview
The program takes a `csv` file containing assignment data, student names, and urls for assignment submissions on GitHub, then automates the process of creating directories and grading sheets for their submissions.

## Process Description
The script will search the `resources/AssignmentCSVFiles` directory for existing assignment files.  These will show up in the main running menu.  The first row of the selected `assignment.csv` file will be parsed for assignment data used to generate a specific directory structure under the `Gradings` directory. The subsequent rows contain student names, and submission URLs for processing and downloading assignments automatically.

## Folder Organization Concerns

This program is intended to reside inside a single directory where the grader (TA, Instructor, etc.) does all of their grading.  This will mean that each call to the program will either generate a new directory, or update the records for existing assignment directories with the `Grading` directory.  So what does this look like as originally intended by the author.

    - Grading/
        - Homework01_Some_Homework/
        - Homework02_Some_more_homework/
        - Homework03_Even_more_homework/
            - Grades/
                - Student01.md
                - Student02.md
                - Student03.md
            - Instructions/
            - Solutions/
            - Submissions/
                - Student01/
                    - Student01.zip
                - Student02/
                    - Student02.zip
                - Student03/
                    - Student03.zip
    - resources/
        - AssignmentCSVFiles
            - Homework01_Some_Homework.csv
            - Homework02_Some_more_homework.csv
            - Homework03_Even_more_homework.csv
        - GradingMDFiles
            - Homework01_Some_Homework.md
            - Homework02_Some_more_homework.md
            - Homework03_Even_more_homework.md
        student_list.txt
    - TEMPLATES/
    - tyjgrader/
    - run_tyjgrader.py (program script)

## Before running the script: 
- a **copy** of the `TEMPLATE_GradeSheet.md` file must be named and customized to reflect the rubric and grading concerns for that particular assignment, and must be placed in the `GradingMDFiles` directory.
- a **copy** of the `TEMPLATE_Assignment.csv`file must be properly prepared, named, and moved to the `AssignmentCSVFiles` directory

## The Assignment File
- The very first line of the assignment `csv` file contains a comma-separated set of values.  
    ```csv
    new_dir_name, Assignment Title, Date String without commas, name_of_gradesheet_file.md, Grader Name
    ```
    
    In order they are:
    1. `new_dir_name` : The folder name for the assignment directory.  No spaces.
    2. `Assignment Title` : Human readable name/title of the assignment.  This gets populated in the grading sheets
    3. `Date string without commas` : Human readable date string. No commas
    4. `name_of_gradesheet_file.md` : The name of the gradesheet template for the particular assignment
    5. `Grader Name` : Human readable name of the TA/Instructor doing the grading for this assignment.  Theis gets populated in the grading sheets
    
- The remaining lines are entries for each student with the url for their submission:
    ```csv
    student name, https://www.github.com/studentgithubusername/repository
    ```
    

## The GradingSheet File
- The basic template for the grading sheets can be customized.  However there are some "convenience" feild placeholders that should be maintained for "automatic" populating of data during generation.  These are surrounded by `<` and `>` symbols to denote either replacement during processing, or manual replacement during the actual grading process.

## "Parts" of the Process

- #### run_tyjgrader.py
    This is the main entry point for the application.  Run the script as follows:

    ```
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

    - #### <OUTPUT_DIR>
        The generated directory for a particular assignment
        
        - #### Grades
            The directory that holds the Markdown "grading sheets" for each student
        
        - #### Submissions
            Directory with individual directories for each student that contain the downloaded submissions
    
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

## Additional Notes
- If you are intending to store your grades and student submissions in a git repository or on a remote repository hosting service (such as GitHub, or others) then be sure to edit the `.gitignore` file to allow the tracking of the `.zip` files in the student submissions.
- Running the process on existing assignments (whith existing directories, and such) will only update "new" submissions from the assignment file.  Existing submissions will not be overwritten.
- If you need to update a submission consider either removing the original submission `grade_sheet` and `url` in the assignment csv file, or adding a second entry for the same student (using a variation on their name to indicate the different submission.)
- If you are unclear about some fo the specifics, I encourage you to run a few tests using the test `assignment` to see how the script works.


## If An Error Occurs

- Delete the folder for that assignment and try again and check the formatting of your `assignment.csv` and `grade_sheet.md` files for that particular assignment. Be sure to follow the template form exactly.

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