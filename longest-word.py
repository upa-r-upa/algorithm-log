import re

def LongestWord(sen):
  words = sen.split(" ")
  longest = ""
  
  for word in words:
    text = re.match(r"[a-zA-Z0-9]+", word)
    
    if len(text.group()) > len(longest):
      longest = text.group()

  return longest

# keep this function call here 
print(LongestWord(input()))