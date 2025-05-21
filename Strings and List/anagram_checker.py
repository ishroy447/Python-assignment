def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        bool: True if strings are anagrams, False otherwise
    """
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if lengths are equal
    if len(str1) != len(str2):
        return False
    
    # Create character frequency dictionaries
    char_count1 = {}
    char_count2 = {}
    
    # Count characters in both strings
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Compare character frequencies
    return char_count1 == char_count2

# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("listen", "silent"),
        ("hello", "world"),
        ("anagram", "nagaram"),
        ("python", "typhon"),
        ("", "")
    ]
    
    for str1, str2 in test_cases:
        result = are_anagrams(str1, str2)
        print(f"Are '{str1}' and '{str2}' anagrams? {result}") 