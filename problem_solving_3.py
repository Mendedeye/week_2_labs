#Task 1: Happy Numbers

def digit_invariant(number):
    total = 0
    for digit in number:
        total += pow(int(digit),2)

    return total

user_input = input("\nPlease enter in a number: ")
result = digit_invariant(user_input)
print(result)