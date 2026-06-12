char=input("Enter anu Character:")
if(char>='A' and char<='Z'):
    char=char.lower()
    print("The entered character was in uppercase. In lowecase it is :",char)
else:
    char=char.upper()
    print("The entered character was in lowercase. In uppercase it is:"+char)