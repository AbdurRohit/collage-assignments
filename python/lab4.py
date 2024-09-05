from collections import Counter

# 1. Program for string manipulation
def string_manipulation():
    input_str = "India is my motherland. I love my country. Capital of India is New Delhi."
    print(f"Length of the string: {len(input_str)}")
    
    # Find the substring "country"
    substring = "country"
    if substring in input_str:
        print(f"'{substring}' is found in the input string.")
    
    # Count the occurrences of each word
    words = input_str.split()
    word_count = Counter(words)
    print("Word occurrences:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

# 2. Program to sort comma-separated words
def sort_words():
    input_str = "without,hello,bag,world"
    words = input_str.split(',')
    words.sort()
    print("Sorted words:", ','.join(words))

# 3. Program to capitalize lines of input
def capitalize_lines():
    lines = ["Hello world", "Practice makes perfect"]
    capitalized_lines = [line.upper() for line in lines]
    print("\n".join(capitalized_lines))

# 4. Program to remove duplicate words and sort
def remove_duplicates_and_sort():
    input_str = "hello world and practice makes perfect and hello world again"
    words = input_str.split()
    unique_words = sorted(set(words))
    print(" ".join(unique_words))

# 5. Program to count letters and digits
def count_letters_digits():
    input_str = "hello world! 123"
    letters = sum(c.isalpha() for c in input_str)
    digits = sum(c.isdigit() for c in input_str)
    print(f"LETTERS {letters}")
    print(f"DIGITS {digits}")

# 6. Program to check if input is "Yes"
def check_yes(input_str):
    if input_str in ["yes", "YES", "Yes"]:
        print("Yes")
    else:
        print("No")

# 7. Program to find words composed of digits only
def find_digit_words():
    input_str = "2 cats and 3 dogs."
    words = input_str.split()
    digit_words = [word for word in words if word.isdigit()]
    print(digit_words)

# 8. Program to count each character in a string
def count_characters():
    input_str = "abcdefgabc"
    char_count = Counter(input_str)
    for char, count in char_count.items():
        print(f"{char},{count}")

# 9. Various string manipulations
def string_operations(input_str, substr, anagram_check_str):
    # 1. Reverse the string
    reversed_str = input_str[::-1]
    print(f"Reversed string: {reversed_str}")

    # 2. Check if it's a palindrome
    is_palindrome = input_str == reversed_str
    print(f"Is palindrome: {is_palindrome}")

    # 3. Check if it ends with a specific substring
    ends_with_substr = input_str.endswith(substr)
    print(f"Ends with '{substr}': {ends_with_substr}")

    # 4. Capitalize the first letter of each word
    capitalized_str = input_str.title()
    print(f"Capitalized: {capitalized_str}")

    # 5. Check if the input string is an anagram of another string
    is_anagram = sorted(input_str) == sorted(anagram_check_str)
    print(f"Is anagram of '{anagram_check_str}': {is_anagram}")

    # 6. Remove vowels from string
    vowels = 'aeiouAEIOU'
    no_vowels_str = ''.join([char for char in input_str if char not in vowels])
    print(f"String without vowels: {no_vowels_str}")

    # 7. Find length of the longest word in a sentence
    longest_word_length = max(len(word) for word in input_str.split())
    print(f"Length of the longest word: {longest_word_length}")

# Main method to call all the functions
if __name__ == "__main__":
    print("Task 1:")
    string_manipulation()
    print("\nTask 2:")
    sort_words()
    print("\nTask 3:")
    capitalize_lines()
    print("\nTask 4:")
    remove_duplicates_and_sort()
    print("\nTask 5:")
    count_letters_digits()
    print("\nTask 6:")
    check_yes("Yes")
    print("\nTask 7:")
    find_digit_words()
    print("\nTask 8:")
    count_characters()
    print("\nTask 9:")
    string_operations("madam", "am", "adamm")