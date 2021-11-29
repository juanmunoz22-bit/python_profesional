def is_palindrome(string: str) -> bool:
    """Find if a word is palindrome or not

    Args:
        string (str): word passed as parameter

    Returns:
        bool: Returns a boolean with the answer
    """    
    string = string.replace(' ', '').lower()
    return string == string[::-1]

def run():
    print(is_palindrome('ana'))

if __name__ == '__main__':
    run()

