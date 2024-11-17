def merge_words(w1, w2):
    temp_str = ""

    l_w1 = len(w1)
    l_w2 = len(w2)

    max_len = max(l_w1, l_w2)

    for i in range(max_len):
        if i < l_w1:
            temp_str += w1[i]
        if i < l_w2:
            temp_str += w2[i]

    return temp_str


word1 = input("Enter word1: ")
word2 = input("Enter word2: ")

merged = merge_words(word1, word2)
print(merged)
