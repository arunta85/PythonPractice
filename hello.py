def main():
    while True:
        name = input("What is your name? ").strip()
        if name:
            print(f"Hello, {name.capitalize()}!")
            break
        else:
            print("Please enter a valid name.")

if __name__ == "__main__":
    main()