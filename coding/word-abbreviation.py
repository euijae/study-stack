def recurse(word, abbr, w, a):
    if a < len(abbr) and abbr[a].isdigit():
        skip = 0
        while a < len(abbr) and abbr[a].isdigit():
            skip = skip * 10 + int(abbr[a])
            a += 1
        w += skip
        if w > len(word):
            return False
        return recurse(word, abbr, w, a)
    
    if a == len(abbr):
        return w == len(word)
    
    if abbr[a] == '*':
        return recurse(word, abbr, w, a + 1) or recurse(word, abbr, w + 1, a)
    
    if w < len(word) and word[w] == abbr[a]:
        return recurse(word, abbr, w + 1, a + 1)
    
    return False

def validWordAbbreviation(word, abbr):
    return recurse(word, abbr, 0, 0)

# Test cases
tests = [
    ("helzzpme", "h2*p*me", True)
]

for word, abbr, expected in tests:
    assert validWordAbbreviation(word, abbr) == expected

print('All passed :green')