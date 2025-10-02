def main():
    text = "  Hello, PythonPractice!  "

    print("Original string:", repr(text))

    # 1. strip (remove spaces at start and end)
    print("strip():", text.strip())

    # 2. lower (all lowercase)
    print("lower():", text.lower())

    # 3. upper (all uppercase)
    print("upper():", text.upper())

    # 4. title (capitalize each word)
    print("title():", text.title())

    # 5. replace (replace part of string)
    print("replace():", text.replace("PythonPractice", "World"))

    # 6. split (break into list of words)
    print("split():", text.split())

    # 7. join (combine list into string)
    words = ["Python", "is", "fun"]
    print("join():", "-".join(words))

    # 8. find (index of substring, -1 if not found)
    print("find('Python'):", text.find("Python"))

    # 9. count (number of times substring appears)
    print("count('l'):", text.count("l"))

    # 10. startswith / endswith
    print("startswith('  He'):", text.startswith("  He"))
    print("endswith('!  '):", text.endswith("!  "))

    # 11. isalpha, isdigit, isnumeric, isalnum
    sample = "Python3"
    print("isalpha():", sample.isalpha())  # only letters?
    print("isdigit():", sample.isdigit())  # only digits?
    print("isalnum():", sample.isalnum())  # letters+digits?

    # 12. len (length of string)
    print("len():", len(text))

    # 13. slicing
    print("Slicing [2:7]:", text[2:7])
    print("Reverse string:", text[::-1])


if __name__ == "__main__":
    main()
