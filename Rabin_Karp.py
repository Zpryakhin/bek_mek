t = input("Введите текст\n")
p = input("Введите подстроку\n")
def find_all_rabin_karp(text, pattern):
    result = []
    patternsum = sum(ord(s) for s in pattern)
    for i in range(len(text) - len(pattern) + 1):
        textwindowsum = sum(ord(text[j+i]) for j in range(len(pattern)))
        if patternsum == textwindowsum:
            if text.startswith(pattern, i):
                result.append(i)
    return result        

print(find_all_rabin_karp(t, p))