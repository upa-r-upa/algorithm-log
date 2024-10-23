def FindIntersection(strArr):
  split_word = ", "
  a_arr = strArr[0].split(split_word)
  b_arr = strArr[1].split(split_word)

  a_dict = dict()
  result = []

  for word in a_arr:
    a_dict[word] = word

  for word in b_arr:
    if word in a_dict:
      result.append(word)

  return ",".join(result) if result else "false"

# keep this function call here 
print(FindIntersection(input()))