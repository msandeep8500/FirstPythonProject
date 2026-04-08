#Counter value -> Check each letter how many times is used
from collections import Counter
def counterCheck(text):
    text=text.lower().replace(" ","")
    return Counter(text)

def sorted_string(w1,w2):
    s1 = sorted(w1.lower().replace(" ",""))
    s2 = sorted(w2.lower().replace(" ",""))
    return s1 == s2

#Counter check testing
text = "Python Programming"
print(f"Counter check': {counterCheck(text)}")

# Anagram testing

def is_anagram(str1, str2):
    # Clean and sort both strings
    s1 = sorted(str1.lower().replace(" ", ""))
    s2 = sorted(str2.lower().replace(" ", ""))
    
    # If the sorted lists are identical, they are anagrams
    return s1 == s2

w1, w2 = "listen", "silents"
result = is_anagram(w1, w2)

print(f'Is "{w1}" an anagram of "{w2}"? {result}')
