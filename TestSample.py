#Enter Python code here and hit the Run button.
words = ["apple", "bat", "cherry", "dog", "elderberry"]
filter_words =[w.upper() for w in words if len(words)/2!=0]
print(filter_words)