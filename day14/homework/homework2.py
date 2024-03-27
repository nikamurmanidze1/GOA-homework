def word(w):
    w = w.lower()
    if w == w[::-1]:
        print(f"{w} is a palpindrom")
    else:
        print(f"{w} is not a palpindrom")
word1 = "kanafi"
word(word1)