import re

def CodelandUsernameValidation(strParam):
  match = re.match(r"^([a-zA-Z]\w{2,23}[a-zA-Z0-9])$", strParam)

  return "true" if match else "false"

# keep this function call here 
print(CodelandUsernameValidation(input()))