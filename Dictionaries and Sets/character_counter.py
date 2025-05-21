def count_characters(text):
    # Create a dictionary to store character frequencies
    char_freq = {}
    
    # Count frequency of each character (excluding spaces)
    for char in text:
        if char != ' ':  # Skip spaces
            char_freq[char] = char_freq.get(char, 0) + 1
    
    return char_freq

def main():
    # Get input from user
    text = input("Enter a string: ")
    
    # Count character frequencies
    frequencies = count_characters(text)
    
    # Display results
    print("\nCharacter Frequencies:")
    print("-" * 30)
    for char, count in sorted(frequencies.items()):
        print(f"'{char}': {count}")

if __name__ == "__main__":
    main() 