def count_vowels_consonants(str):
    str = str.lower()
    count_vowel = 0
    count_consonant = 0
    for ch in str:
        if ch in ['a','e','i','o','u']:
            count_vowel += 1
        else:
            if ch.isalpha():
                count_consonant += 1
    print(f"Vowels: {count_vowel}\nConsonants: {count_consonant}")

user_input = input("Enter the string:")
count_vowels_consonants(user_input)