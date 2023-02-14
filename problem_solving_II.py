#Task 1: Reverse a String
def reverse_string():
    reversed_string = ""
    user_string = input("Please enter in a string for me to reverse: ")

    for index in range(len(user_string) -1, -1, -1):
        reverse_string += user_string[index]

    return reverse_string



#Task 2: Capitalize a Letter

#Task 3:  Palindrome

#Task 4(bonus): Compress a string of characters