def reverseStr(string):
   if len(string) == 1:
      return string[0]
   else:
      return reverseStr(string[1:]) + string[0]

print(reverseStr('hello'))