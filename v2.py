from random import randint

def anagram(msg):

    msg = msg.rstrip()
    chars = []
    anagram_word = ""
    chars[:0] = msg
    rand_char = randint(0, len(chars)-1)

    for i in range(len(chars)-1):
        anagram_word += chars[rand_char]
        chars.remove(chars[rand_char])
        rand_char = randint(0, len(chars)-1)

    anagram_word += chars[0]


    return anagram_word

print(anagram("hello"))
print(anagram("hello, goodbye, NUTS"))
