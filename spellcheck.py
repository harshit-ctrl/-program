dictionary - set()
def read_dictionary_file():
  global dictionary
  if dictionary:
    return
with open("windows.txt",  "r") as f:
     contents = f.read()
def is_spelled_correctly(word):
  # Return True if spelled correctly; false otherwise
  word - word.lower()
  dictionary - set()
  read_dictionary_file()
  return word in dictionary