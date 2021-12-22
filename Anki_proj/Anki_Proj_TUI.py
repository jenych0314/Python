import string

while True:
    print("""Enter the English word
    If you want to quit then pls enter the \'quit\'.
    -> """)
    input_word = input().lower().strip()

    if input_word not in string.ascii_letters:
        print("pls enter the English word")
    if input_word == "quit":
        break
