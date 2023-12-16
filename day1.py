def update_str_for_digits(str):
    digits_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    str = str.strip()
    pt1 = 0
    pt2 = 1
    new_str = str.strip()
    changed_index = 0
    while pt2 <= len(str):
        if str[pt1].isdigit():
            pt1 = str.find(str[pt1], pt1, pt2) + 1
            pt2 = pt1 + 1
            continue
        if str[pt1:pt2 + 1] in digits_map:
            start_ind = changed_index if changed_index else pt1
            new_str = new_str.replace(
                str[start_ind:pt2 + 1], digits_map[str[pt1:pt2 + 1]])
            pt1 = pt2
            changed_index = pt1 + 1

        if pt2 - pt1 >= 4:
            pt1 += 1
            pt2 = pt1 + 1
        else:
            pt2 += 1

    pt1 = len(str.strip()) - 1
    pt2 = pt1 - 1
    while pt2 >= 0:
        if str[pt1].isdigit():
            pt1 -= 1
            pt2 -= 1
            continue
        if str[pt2:pt1 + 1] in digits_map:
            new_str = new_str.replace(
                str[pt2:pt1 + 1], digits_map[str[pt2:pt1 + 1]])
            pt1 = pt2
        if pt1 - pt2 >= 4:
            pt1 -= 1
            pt2 = pt1 - 1
        else:
            pt2 -= 1
    print(f'old: {str}, and new: {new_str}')
    return new_str


def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    sum = 0
    for i in range(len(lines)):
        updated_str = update_str_for_digits(lines[i])
        pt1 = 0
        pt2 = len(updated_str) - 1
        flag = False
        while pt1 <= pt2:
            if (updated_str[pt1].isdigit() and
                    updated_str[pt2].isdigit()):
                flag = True
                break
            if not updated_str[pt1].isdigit():
                pt1 += 1
            if not updated_str[pt2].isdigit():
                pt2 -= 1

        if flag:
            sum += int(updated_str[pt1] + updated_str[pt2])

    return sum


if __name__ == "__main__":
    print(main())
    # update_str_for_digits('eight5fourtwotwo')
