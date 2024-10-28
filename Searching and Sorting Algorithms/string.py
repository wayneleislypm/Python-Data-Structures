'''Write a python program that takes an input from the user and if they are any spaces btwn the input string it replaces with *%20* else it prints "excellent input" '''
sentence = input("Enter your text: ")
if (" " or "_") in sentence:
    x = sentence.replace(" ","%20")
    x = x.replace("_","+")
    print(x)
else:
      print("That's an excellent input")