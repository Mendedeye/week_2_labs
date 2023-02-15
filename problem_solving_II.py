#Task 1: Reverse a String
def reverse_string():
    reversed_string = ""
    user_string = input("\n\nPlease enter in a string for me to reverse: ")

    for index in range(len(user_string) -1, -1, -1):
        reversed_string += user_string[index]

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
def determine_palindrome():
    user_string = input("\n\nPlease enter in a word that is palindrome(a word that is read the same forwards and backwards): ")
    is_palindrome = False
    positive_index = 0
    negative_index = -1

    while is_palindrome == False:
        if user_string[positive_index] == user_string[negative_index] and positive_index < (len(user_string)/2):
            if positive_index == int(len(user_string)/2):
                is_palindrome = True
            positive_index += 1
            negative_index -= 1

        else:
            user_string = input("Please enter in a palindrome word: ")

    return user_string

#Task 4(bonus): Compress a string of characters
def compress_string():
    compressed_string = ""
    next_index = 1
    counter = 0
    user_string = input("Put a bunch of repeating characters in here, have fun: ")

    for current_index in range(len(user_string)):
        if next_index == len(user_string):
            counter += 1
            compressed_string += str(counter)
            compressed_string += user_string[current_index]
            break
        elif user_string[current_index] == user_string[next_index]:
            counter += 1
            next_index += 1
        else:
            counter += 1
            compressed_string += str(counter)
            compressed_string += user_string[current_index]
            next_index += 1
            counter = 0
    
    return compressed_string

#Run all functions
def run_functions():
    #Task 1
    reverse_string()

    #Task 2
    capitalized_string = ""
    capitalized_string = capitalize_first_letter()
    print(capitalized_string)

    #Task 3
    palindrome_word = determine_palindrome()
    print(f"Your palindrome word is {palindrome_word}")

    #Task 4
    compressed_string  = compress_string()
    print(compressed_string)

run_functions()