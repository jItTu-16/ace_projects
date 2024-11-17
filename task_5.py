keypad = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


def cross(a, b):
    temp_list = []

    for i in a:
        for j in b:
            temp_list.append(i + j)

    return temp_list


def solve(digits):

    if digits == "":
        return []
    if len(digits) == 1:
        return keypad.get(digits)

    temp_list = cross(keypad.get(digits[0]), keypad.get(digits[1]))

    for i in range(2, len(digits)):
        temp_list = cross(temp_list, keypad.get(digits[i]))

    return temp_list


nums = input("Enter numbers: ")
print(solve(nums))
