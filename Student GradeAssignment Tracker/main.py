"""Main program for the Student Grade/Assignment Tracker."""

from student_tracker import StudentTracker


def display_menu():
    """Show the available menu options."""
    print("===========================")
    print("Student Grade Tracker")
    print("===========================")
    print("1. Add Homework")
    print("2. Add Exam")
    print("3. List Assignments")
    print("4. Filter Assignments")
    print("5. Show Summary")
    print("6. Exit")
    print()


def main():
    """Run the interactive menu loop."""
    tracker = StudentTracker()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            tracker.add_homework()
        elif choice == "2":
            tracker.add_exam()
        elif choice == "3":
            tracker.list_assignments()
        elif choice == "4":
            tracker.filter_assignments()
        elif choice == "5":
            tracker.show_summary()
        elif choice == "6":
            print("Thank you for using Student Grade Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose from 1 to 6.\n")


if __name__ == "__main__":
    main()
