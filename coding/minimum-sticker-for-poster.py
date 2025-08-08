import math

def minimum_sticker_for_poster(sticker, poster):
    sticker_freqs = {}
    for letter in sticker:
        sticker_freqs[letter] = sticker_freqs.get(letter, 0) + 1
    poster_freqs = {}
    for letter in poster:
        poster_freqs[letter] = poster_freqs.get(letter, 0) + 1
    print(sticker_freqs)
    print(poster_freqs)
    count = 0
    for letter, freqs in poster_freqs.items():
        if letter not in sticker_freqs:
            return -1
        count = max(count, math.ceil(freqs / sticker_freqs[letter]))
    
    return count

print(minimum_sticker_for_poster(['a', 'b', 'c', 'c'], ['a', 'b', 'b', 'c', 'c', 'c', 'c', 'c']))