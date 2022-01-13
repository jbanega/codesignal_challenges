def validator(sequence):
    """This functions validate if a sequence of different types of brackets is correct"""

    brackets = {
        "left": "([{",
        "right": ")]}"
    }

    order = []
    is_valid = False

    for n, char in enumerate(sequence):

        if n == len(sequence):
            break

        if (char not in brackets["left"]) and (char not in brackets["right"]):
            is_valid = False
            return is_valid

        if (n == 0) and (char in brackets["right"]):
            is_valid = False
            return is_valid

        if char in brackets["left"]:
            if char == "(":
                order.append(0)
            elif char == "[":
                order.append(1)
            else:
                order.append(2)
            continue

        elif char in brackets["right"]:
            index = brackets["right"].index(char)
            if index != order[-1]:
                is_valid = False
                return is_valid
            else:
                order.pop()
                continue
    
    is_valid = True
    return is_valid


if __name__ == "__main__":
    test = [
        ("()", True),
        ("()[]{}", True),
        ("([])", True),
        ("{[)]", False),
        ("([]}", False)
    ]

    i = 1
    for entry, expected_output in test:
        result = validator(entry)
        if result != expected_output:
            print(f"Test {i} - {entry} - Output: {result} - Fail")
        else:
            print(f"Test {i} - {entry} - Output: {result} - Pass")
        i += 1