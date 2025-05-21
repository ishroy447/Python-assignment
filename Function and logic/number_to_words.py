def number_to_words(num):
    """Convert a number to its word representation."""
    if num == 0:
        return "zero"
    
    # Define word mappings
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
            "eighty", "ninety"]
    
    def convert_less_than_thousand(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + ("-" + ones[n % 10] if n % 10 != 0 else "")
        else:
            return ones[n // 100] + " hundred" + (" and " + convert_less_than_thousand(n % 100) if n % 100 != 0 else "")
    
    def convert(n):
        if n < 1000:
            return convert_less_than_thousand(n)
        elif n < 1000000:
            return convert_less_than_thousand(n // 1000) + " thousand" + (" " + convert_less_than_thousand(n % 1000) if n % 1000 != 0 else "")
        elif n < 1000000000:
            return convert_less_than_thousand(n // 1000000) + " million" + (" " + convert(n % 1000000) if n % 1000000 != 0 else "")
        else:
            return convert_less_than_thousand(n // 1000000000) + " billion" + (" " + convert(n % 1000000000) if n % 1000000000 != 0 else "")
    
    return convert(num)

# Example usage
if __name__ == "__main__":
    # Test the function with some numbers
    test_numbers = [0, 5, 15, 25, 100, 123, 1000, 1234, 10000, 12345, 100000, 123456]
    for num in test_numbers:
        print(f"{num}: {number_to_words(num)}") 