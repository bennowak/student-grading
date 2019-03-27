# student-grading
**A python module to simplify student grading from GitHub submissions**

## Overview
The module takes a list of students and automates the process of creating directories for their submissions, followed by downloading theier respective GitHub project archived zip files.

## test.py
This script takes the following arguments in the specific formats given

- Assignment name starting with `Homework`, `Project`, `Classwork`, `Bonus` or some other capitalized single word.  The next sequence is a two digit number.  NOTE: Single digits should be prepended with a zero `0`. Then followed with a descriptive title.  All words are to be separated b a single underscore character `_`.  To sumarize, it is absolutely mandatory that the format is in the following general format:  `Word_01_Some_Title_Here`

- A relative path from the directory which this script is in to the text file containing the list of students. (See Students.txt format notes below.)
- A relative path from the directory which this script is in to the markdown file that is the "template" for the assignment. (See AssignmentGradingTEMPLATE.md description and formatting notes below.)
- A series of key/value arguments, with keys requiring quotes and surrounded by <> symbols (ie : `"<name>"`).  The keys are :
  
    - `<name>` - The value of this key is non-relevant, and just a place holder, so `null` is fine.
    - `<assignment` - A string literal (in quotes) that will be the printed title of the assignment on generated grading sheets
    - `<due>` - A date value. TBD // ToDo:
    
### Running the script

The general call signature is as follows:

```
python test.py <Underscore_Title> "<dateAsString>" <pathToStudenstFile> <pathToMarkDownTEMPLATE>
```
_**EXAMPLE**_
```
python test.py HW_03_Python resources/students.txt resources/TEMPLATEAssignmentGrading.md "<name>" null "<assignment>" "Homework - 03 Python" "<due>" 20190321
```
## Output

Given the following student file : 
```angular2
Bee Gud
Som Purrsen
Jam Out
```

unning the example command at the command line will yield the following structure : 

![The Output](docs/Output.png)
