"""Main logic for the Student Grade/Assignment Tracker."""

from assignment import Exam, Homework


class StudentTracker:
    """Manage a list of homework and exam entries."""

    def __init__(self):
        """Initialize an empty list of assignments."""
        self.assignments = []

    def add_homework(self):
        """Collect homework details and store a Homework object."""
        print("\nAdd Homework")
        print("------------")
        title = input("Enter assignment title: ")
        date = input("Enter date (e.g. 2026-08-03): ")
        score = self._get_valid_score()
        max_score = self._get_valid_max_score()
        description = input("Enter description: ")

        homework = Homework(title, date, score, max_score, description)
        self.assignments.append(homework)
        print("Homework added successfully.\n")

    def add_exam(self):
        """Collect exam details and store an Exam object."""
        print("\nAdd Exam")
        print("--------")
        title = input("Enter exam title: ")
        date = input("Enter date (e.g. 2026-08-03): ")
        score = self._get_valid_score()
        max_score = self._get_valid_max_score()
        description = input("Enter description: ")

        exam = Exam(title, date, score, max_score, description)
        self.assignments.append(exam)
        print("Exam added successfully.\n")

    def list_assignments(self):
        """Display every stored assignment."""
        if not self.assignments:
            print("No assignments recorded yet.\n")
            return

        print("\nAll Assignments")
        print("---------------")
        for assignment in self.assignments:
            print(assignment.display())
            print("-" * 25)

    def filter_assignments(self):
        """Show assignments matching a selected category."""
        if not self.assignments:
            print("No assignments recorded yet.\n")
            return

        category = input("Enter category to filter (Homework or Exam): ").strip()

        print(f"\nAssignments for category: {category}")
        print("-------------------------------")
        found = False

        for assignment in self.assignments:
            if assignment.category.lower() == category.lower():
                print(assignment.display())
                print("-" * 25)
                found = True

        if not found:
            print("No matching assignments found.\n")

    def show_summary(self):
        """Calculate and print average percentage for all assignments."""
        if not self.assignments:
            print("No assignments recorded yet.\n")
            return

        total_percentage = 0.0
        for assignment in self.assignments:
            total_percentage += assignment.calculate_percentage()

        average_percentage = total_percentage / len(self.assignments)

        print("\nGrade Summary")
        print("------------")
        print(f"Total Assignments: {len(self.assignments)}")
        print(f"Average Percentage: {average_percentage:.1f}%")
        print()

    def _get_valid_score(self):
        """Ensure the score entered is a positive number."""
        while True:
            try:
                score = float(input("Enter score: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if score < 0:
                print("Score cannot be negative.")
            else:
                return score

    def _get_valid_max_score(self):
        """Ensure the maximum score is a positive number."""
        while True:
            try:
                max_score = float(input("Enter maximum score: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if max_score <= 0:
                print("Maximum score must be greater than zero.")
            else:
                return max_score
