def word_counter(text):

    # print("Entered string: ", text)
    list = text.split()
    # print(list)
    ln_list = len(list)

    return ln_list


x = 1
while x:

    str1 = input("Enter any string: ")
    count = word_counter(str1)
    print("Number of word in given string are....", count)

    while True:
        rep = input("Do you want to check anothor string (y/n): ")

        if rep == "y":
            break
        elif rep == "n":
            x = 0
            break
        else:
            print("Enter valid response")
