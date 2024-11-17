def add_linked_list(ls1, ls2):
    len_ls1 = len(ls1)
    len_ls2 = len(ls2)

    max_len = max(len_ls1, len_ls2)

    result = []

    carry = 0

    for i in range(max_len):
        a = 0
        b = 0

        if i < len_ls1:
            a = ls1[i]
        if i < len_ls2:
            b = ls2[i]

        s = a + b + carry

        carry, ones = divmod(s, 10)

        result.append(ones)

    if carry != 0:
        result.append(carry)

    return result


ls1 = [9, 9, 9, 9, 9, 9, 9]
ls2 = [9, 9, 9, 9]
print(add_linked_list(ls1, ls2))
