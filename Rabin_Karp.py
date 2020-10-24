t = input("Введите текст\n")
p = input("Введите подстроку\n")
def find_all_rabin_karp(text, pattern):
    result = []
    patternsum = sum(ord(s) for s in pattern)
    textwindowsum = sum(ord(text[j]) for j in range(len(pattern)))
    for i in range(len(text) - len(pattern) + 1):
        textwindowsum = textwindowsum - ord(text[i])+ord(text[i+len(pattern)-1])  
        if patternsum == textwindowsum:
            if text.startswith(pattern, i):
                result.append(i)
              
    return result        

print(find_all_rabin_karp(t, p))