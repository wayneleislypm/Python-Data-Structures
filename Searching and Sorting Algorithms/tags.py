import re
from pythonds.basic.stack import Stack

expr = "<[a-z]+|</[a-z]+"
file = open("html.txt", "r")
contents = file.read()

tags = re.findall(expr, contents)

tags = list(map(lambda x: x.strip('</') if '</' in x else x.strip('<'), tags))
stack = Stack()
print(tags)
for tag in tags:
    if tag == "img":
        print("Img is self closing")
    elif not stack.isEmpty():
        if stack.peek() == tag:
            stack.pop()
        else:
            stack.push(tag)
    else:
        stack.push(tag)
    print(stack.size())
print(stack.size())
