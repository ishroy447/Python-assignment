def flatten_list(nested_list: list) -> list:
    """
    Flatten a nested list structure.
    
    Args:
        nested_list (list): Input nested list
        
    Returns:
        list: Flattened list
    """
    flattened = []
    
    def _flatten(items):
        for item in items:
            if isinstance(item, list):
                _flatten(item)
            else:
                flattened.append(item)
    
    _flatten(nested_list)
    return flattened

# Example usage
if __name__ == "__main__":
    test_lists = [
        [1, [2, 3], [4, [5, 6]]],
        [[1, 2], [3, 4], [5, 6]],
        [1, 2, 3, 4, 5],
        [[[1]]],
        []
    ]
    
    for test_list in test_lists:
        result = flatten_list(test_list)
        print(f"\nOriginal list: {test_list}")
        print(f"Flattened list: {result}") 