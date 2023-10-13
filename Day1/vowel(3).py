def string(strng):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0

    for char in strng:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

strng=input("Enter String:")
string(strng)

vowel_count, consonant_count = string(strng)

print(f"String: {strng}")
print(f"Vowel count: {vowel_count}")
print(f"Consonant count: {consonant_count}")
'''
Enter String:malayalam
String: malayalam
Vowel count: 4
Consonant count: 5
'''