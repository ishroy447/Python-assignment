def count_file_stats(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split('\n')
            
            # Count words (split by whitespace and filter out empty strings)
            words = [word for line in lines for word in line.split() if word]
            
            # Count characters (including spaces and newlines)
            char_count = len(content)
            
            # Count lines (excluding empty lines)
            line_count = len([line for line in lines if line.strip()])
            
            print(f"File Statistics for {filename}:")
            print(f"Total Words: {len(words)}")
            print(f"Total Lines: {line_count}")
            print(f"Total Characters: {char_count}")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    filename = "sample.txt"
    count_file_stats(filename) 