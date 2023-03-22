text = input()

pattern = "happy"
cnt = 0
for i in range(len(text) - len(pattern) + 1):
    found = True

    for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
            found = False
            break

    if found:
        cnt=cnt+1

print(cnt)