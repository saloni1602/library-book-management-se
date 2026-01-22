# Library Book Management System

## Course Details
- Course Code: CS2042 – Software Engineering
- Assignment: Task 1 – Agile Development with Git and Unit Testing
- Student Name: Saloni Kumari
- Roll Number: 240101054
- Institution: IIIT Manipur

---

## Introduction
This project is a Library Book Management System developed as part of the Software Engineering course. The main objective of this assignment is to apply Agile development practices, Git version control, unit testing, and traceability in a small but complete software system.

The application is implemented using Python and uses only in-memory data structures. No database or external libraries are used.

---

## Agile Development Approach
The project follows an Agile sprint-based development model. The work is divided into three sprints. Each sprint delivers a working feature, which is tested, merged into the main branch, and tagged as a release.

Sprint discipline was strictly followed:
- Separate branch for each sprint
- Unit tests written for every sprint
- Code merged only after tests passed
- Release tags created after every sprint

---

## Sprint-wise Features

### Sprint-1 (v0.1): Book Registration
Features implemented:
- Add a book with Book ID, Title, and Author
- Prevent addition of duplicate Book IDs

Key function:
- add_book(book_id, title, author)

---

### Sprint-2 (v0.2): Borrow and Return Book
Features implemented:
- Borrow a book
- Return a book
- Prevent borrowing of an already borrowed book

Key functions:
- borrow_book(book_id)
- return_book(book_id)

---

### Sprint-3 (v0.3): Library Report
Features implemented:
- Generate a library report displaying:
  - Book ID
  - Title
  - Author
  - Status (Available / Borrowed)

Key function:
- generate_report()

---

## Project Structure

library-se/
├── src/
│   └── library.py        (Main application code)
├── tests/
│   └── test_library.py   (Unit tests for all sprints)
├── docs/
│   ├── USER_STORIES.md
│   └── TRACEABILITY.md
├── README.md
└── .gitignore

---

## Technologies Used
- Programming Language: Python 3
- Testing Framework: unittest
- Version Control System: Git and GitHub
- Development Model: Agile (Sprint-based)

---

## Unit Testing
Unit testing is done using Python’s built-in unittest framework. For every sprint, test cases were written to verify the correctness of the implemented features.

All tests were executed before merging sprint branches into the main branch.

### Command to Run Tests
Run the following command from the project root directory:

python -m unittest discover -s tests -p "test_*.py" -v

---

## Git Workflow Followed
- Git repository initialized locally
- Feature branches created for each sprint:
  - feature/sprint-1
  - feature/sprint-2
  - feature/sprint-3
- Sprint branches merged into main branch
- Release tags created:
  - v0.1 after Sprint-1
  - v0.2 after Sprint-2
  - v0.3 after Sprint-3

---

## Traceability
A traceability matrix is maintained in docs/TRACEABILITY.md. It links:
- User stories
- Implementation code
- Unit tests
- Release tags

This ensures that all requirements are implemented and verified.

---

## Learning Outcome
Through this assignment, I gained practical experience in Agile development, Git version control, unit testing, and traceability. The assignment helped me understand how real-world software projects are developed incrementally with proper testing and version control.

---

## GitHub Repository
The complete project including source code, unit tests, documentation, branches, and tags is available in the GitHub repository.
