#Task 1: Reverse a String
def reverse_string():
    reversed_string = ""
    user_string = input("\n\nPlease enter in a string for me to reverse: ")

    for index in range(len(user_string) -1, -1, -1):
        reverse_string += user_string[index]

    return reverse_string

#Task 2: Capitalize a Letter
def capitalize_first_letter():
    capitalized_string = ""
    user_string = input("\n\nPlease enter in a multiword string and I will capitalize the first letter of every word: ")

    for index in range(len(user_string)):
        if index == 0 and user_string[index] != " ":
            capitalized_string += str(user_string[0].upper())
        elif user_string[index-1] == " ":
            capitalized_string += str(user_string[index].upper())
        else:
            capitalized_string += str(user_string[index])

    return capitalized_string

#Task 3:  Palindrome

#Task 4(bonus): Compress a string of characters
capitalized_string = ""

capitalized_string = capitalize_first_letter()
print(capitalized_string)