import csv

def analyze_student_marks(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            # Check if required columns exist
            required_columns = ['Name', 'Marks']
            header = csv_reader.fieldnames
            if not all(col in header for col in required_columns):
                print("Error: CSV file must contain 'Name' and 'Marks' columns")
                return
            
            # Process student marks
            high_scorers = []
            for row in csv_reader:
                try:
                    marks = float(row['Marks'])
                    if marks >= 75:
                        high_scorers.append((row['Name'], marks))
                except ValueError:
                    print(f"Warning: Invalid marks for student {row['Name']}")
            
            # Display results
            if high_scorers:
                print("\nStudents scoring above 75%:")
                print("-" * 30)
                for name, marks in high_scorers:
                    print(f"{name}: {marks}%")
            else:
                print("No students scored above 75%")
                
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    filename = "student_marks.csv"
    analyze_student_marks(filename) 