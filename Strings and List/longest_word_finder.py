def find_longest_word(sentence: str) -> tuple:
    """
    Find the longest word in a sentence.
    
    Args:
        sentence (str): Input sentence
        
    Returns:
        tuple: (longest_word, length)
    """
    # Remove punctuation and split into words
    words = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in sentence).split()
    
    if not words:
        return ("", 0)
    
    # Find the longest word
    longest_word = max(words, key=len)
    return (longest_word, len(longest_word))

# Example usage
if __name__ == "__main__":
    test_sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Python programming is fun and challenging",
        "Hello, World!",
        "This is a test sentence with some very long words like 'supercalifragilisticexpialidocious'",
        ""
    ]
    
    for sentence in test_sentences:
        longest_word, length = find_longest_word(sentence)
        print(f"\nSentence: {sentence}")
        print(f"Longest word: '{longest_word}'")
        print(f"Length: {length}") 