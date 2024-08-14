# my_package/module2.py

def reverse_string(s):
    """Return the reverse of the given string."""
    return s[::-1]

def capitalize_words(s):
    """Return the string with each word capitalized."""
    return ' '.join(word.capitalize() for word in s.split())

def is_palindrome(s):
    """Check if the given string is a palindrome."""
    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned_string == cleaned_string[::-1]

def count_vowels(s):
    """Count the number of vowels in the given string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
