def palindrom():

    string = input("Enter a string: ")

    check = False
    for i in range(len(string)//2):
        if string[i] == string[len(string) - 1 - i]:
            check = True
        else:
            check = False

    if check:
        print("Palindrome.")
    else:
        print("Not palindrome.")


palindrom()
