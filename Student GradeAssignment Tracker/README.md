# Student Grade / Assignment Tracker

## Project Overview
This project is a beginner-friendly command-line application written in Python 3. It allows a student to enter homework and exam results, view all assignments, filter them by category, and see a summary of their grades.

## Features
- Add homework results
- Add exam results
- List all assignments
- Filter assignments by category
- Show average percentage summary
- Simple menu-based interface
- Input validation for invalid or negative values

## Project Structure
Student GradeAssignment Tracker/
├── main.py
├── assignment.py
├── student_tracker.py
├── README.md
├── repository_link.txt
└── screenshots/

## How to Run
1. Open a terminal.
2. Navigate to the Student GradeAssignment Tracker folder.
3. Run:

```bash
python main.py
```

## Menu Structure
1. Add Homework
2. Add Exam
3. List Assignments
4. Filter Assignments
5. Show Summary
6. Exit

## Sample Interaction
```text
===========================
Student Grade Tracker
===========================
1. Add Homework
2. Add Exam
3. List Assignments
4. Filter Assignments
5. Show Summary
6. Exit

Enter your choice: 1

Add Homework
------------
Enter assignment title: Programming Lab
Enter date (e.g. 2026-08-03): 2026-08-03
Enter score: 18
Enter maximum score: 20
Enter description: Week 4 lab
Homework added successfully.
```

## Screenshots
Screenshots showing add, list, filter, and summary can be added to the screenshots folder.

## Reflection
This project helped me improve my understanding of Python programming by applying key concepts such as classes, inheritance, functions, loops, and input validation. I learned how to break a program into smaller, reusable parts so it is easier to understand and maintain. Building the menu-based system also helped me practise handling user input and responding to different choices clearly.

One of the main challenges was making sure the program worked correctly without crashing when invalid data was entered. I solved this by adding validation checks for scores and maximum marks. I also learned that good program design makes it easier to add new features later, such as saving data to a file or improving the summary reports.

## What I Learned
- How to use classes and inheritance
- How to structure a menu-based command-line program
- How to validate user input safely
- How to keep code modular and readable

## Challenges
- Making the code beginner-friendly
- Handling invalid input without crashing the program
- Organising the project into separate files

## Future Improvements
- Save data to a file
- Add grade letter conversion
- Add sorting by date or category
- Allow editing or deleting entries

## Suggested Git Commit Messages
- Initialise Student Tracker project structure
- Create assignment classes with inheritance
- Implement tracker logic and input validation
- Add menu system and command-line interface
- Add assignment listing and filtering
- Add grade summary calculations
- Write project documentation and usage guide
- Prepare final project files and screenshots folder
