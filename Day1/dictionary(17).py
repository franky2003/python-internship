def get_meaning(word):
    dictionary = {
        "hello": "used as a greeting or to begin a conversation",
        "world": "the earth, together with all of its countries and peoples",
        "python": "a high-level programming language",
        "dictionary": "a book or electronic resource that lists the words of a language"
    }

    return dictionary.get(word.lower())
def main():
    while True:
        word = input("Enter a word (press n to stop): ")
        if word == 'n':
            break

        meaning = get_meaning(word)
        if meaning:
            print(f"Meaning of {word}: {meaning}")
        else:
            print(f"Invalid Word")

main()

#Output
'''
Enter a word (press n to stop): hello
Meaning of hello: used as a greeting or to begin a conversation
Enter a word (press n to stop): World
Meaning of World: the earth, together with all of its countries and peoples
Enter a word (press n to stop): n
'''