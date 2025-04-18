from collections import deque

# Function to check if a string is a palindrome
def is_palindrome(input_string):
    # Convert the string to lowercase and remove spaces
    normalized = input_string.lower().replace(" ", "")
    # Create a double-ended queue of characters
    char_queue = deque(normalized)
    
    # Compare characters from both ends of the queue
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

# Example usage
if __name__ == "__main__":
    test_str = "A man a plan a canal Panama"
    print(is_palindrome(test_str))