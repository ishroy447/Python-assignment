class Gradebook:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name, marks):
        """Add a student and their marks to the gradebook."""
        self.students[name] = marks
    
    def get_marks(self, name):
        """Get marks for a specific student."""
        return self.students.get(name, "Student not found")
    
    def display_all_students(self):
        """Display all students and their marks."""
        if not self.students:
            print("No students in the gradebook.")
            return
        
        print("\nStudent Gradebook:")
        print("-" * 30)
        for name, marks in sorted(self.students.items()):
            print(f"{name}: {marks}")

def main():
    gradebook = Gradebook()
    
    while True:
        print("\nStudent Gradebook Menu:")
        print("1. Add student")
        print("2. Query student marks")
        print("3. Display all students")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter student name: ")
            marks = input("Enter student marks: ")
            gradebook.add_student(name, marks)
            print("Student added successfully!")
            
        elif choice == '2':
            name = input("Enter student name to query: ")
            marks = gradebook.get_marks(name)
            print(f"Marks: {marks}")
            
        elif choice == '3':
            gradebook.display_all_students()
            
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 