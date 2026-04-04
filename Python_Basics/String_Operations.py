def reverse(s):
  return s[::-1]

def count_vowels(s):
  count = 0
  for i in range(len(s)):
    if s[i].lower() in ['a','e','i','o','u']:
      count+=1
    else:
      continue
  return count
def check_palindromes(s):
  if s == s[::-1]:
    return True
  else:
    return False