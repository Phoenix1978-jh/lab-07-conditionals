firstnum= input("Give me a number,any number...: ")
secondnum= input("Okay,give me another number...: ")
operation= input("And what operation do you want? mul/div/mod): ")
#could not use the empty/undeclared variable "answer" from HTML file. omitted for py file.  
#convert variable (string) to number by using float within (()), then wrap whole operation in another()
if operation=="mul":
    print((float(firstnum)) * (float(secondnum)))
elif operation=="div":
    print((float(firstnum)) / (float(secondnum)))
elif operation=="mod": 
    print((float(firstnum)) % (float(secondnum)))
else: 
    print("Invalid operation")