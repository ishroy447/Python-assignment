def count_word_frequency(paragraph):
    # Convert paragraph to lowercase and split into words
    words = paragraph.lower().split()
    
    # Create a dictionary to store word frequencies
    word_freq = {}
    
    # Count frequency of each word
    for word in words:
        # Remove any punctuation from the word
        word = word.strip('.,!?()[]{}":;')
        if word:  # Only count non-empty words
            word_freq[word] = word_freq.get(word, 0) + 1
    
    return word_freq

def main():
    # Get input from user
    print("Enter a paragraph (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    
    paragraph = ' '.join(lines)
    
    # Count word frequencies
    frequencies = count_word_frequency(paragraph)
    
    # Display results
    print("\nWord Frequencies:")
    print("-" * 30)
    for word, count in sorted(frequencies.items()):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main() 