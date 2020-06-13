def myVerify(card_number):

    # 1
    if (int(card_number[0])) != 4:
        return 1

    # 2
    if (int(card_number[3])) > (int(card_number[5])+1):
        return 2

    # 3
    total = 0
    for char in card_number:
        # skip dashes
        if char == '-':
            continue
        total = total + int(char)
    if total % 4 != 0:
        return 3

    # 4
    firstdigits = card_number[0:2]
    seconddigits = card_number[7: 9]
    if int(firstdigits) + int(seconddigits) != 100:
        return 4

    return True

input = "4037-6000-0000"  # change this as you test your function
output = myVerify(input)  # invoke the method using a test input
print(output)  # prints the output of the function
# do not remove this line!
