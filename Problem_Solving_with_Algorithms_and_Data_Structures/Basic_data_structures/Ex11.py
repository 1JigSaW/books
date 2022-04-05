from L_stack import Stack

def parChecker(symbolString):
    s = Stack()
    symbol = ''
    balanced = True
    index = 0
    tags = ['<html>', '<head>', '<title>', '<body>', '<h1>']
    while index < len(symbolString) and balanced:
        if symbolString[index] == '<':
            while symbolString[index] != '>':
                symbol += symbolString[index]
        print(symbol)
        if symbol in tags:
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(parChecker('''
<html>
   <head>
      <title>
         Example
      </title>
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
</html>
'''))