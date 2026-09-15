word1 = input().strip()
word2 = input().strip()

if len(word1) != len(word2):
    print("NO")
else:
    count = {}

    for ch in word1:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    for ch in word2:
        if ch in count:
            count[ch] -= 1
        else:
            count[ch] = -1

    is_anagram = True

    for value in count.values():
        if value != 0:
            is_anagram = False
            break

    if is_anagram:
        print("YES")
    else:
        print("NO")