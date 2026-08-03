"""Assignment models for the Student Grade/Assignment Tracker."""


class Assignment:
    """Base class for homework and exam entries."""

    def __init__(self, title, date, score, max_score, category, description, assignment_type):
        """Store the shared information for an assignment."""
        self.title = title
        self.date = date
        self.score = score
        self.max_score = max_score
        self.category = category
        self.description = description
        self.assignment_type = assignment_type

    def calculate_percentage(self):
        """Return the percentage grade for this assignment."""
        return (self.score / self.max_score) * 100

    def display(self):
        """Return a formatted string for printing in the terminal."""
        percentage = self.calculate_percentage()
        return (
            f"Title: {self.title}\n"
            f"Date: {self.date}\n"
            f"Type: {self.assignment_type}\n"
            f"Score: {self.score}/{self.max_score}\n"
            f"Percentage: {percentage:.1f}%\n"
            f"Category: {self.category}\n"
            f"Description: {self.description}"
        )


class Homework(Assignment):
    """Represents a homework submission."""

    def __init__(self, title, date, score, max_score, description):
        """Initialize a homework item using the parent class."""
        super().__init__(title, date, score, max_score, "Homework", description, "Homework")


class Exam(Assignment):
    """Represents an exam result."""

    def __init__(self, title, date, score, max_score, description):
        """Initialize an exam item using the parent class."""
        super().__init__(title, date, score, max_score, "Exam", description, "Exam")
