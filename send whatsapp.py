def whatsapp():
    number=input("Enter number with country code:")
    msg=input("Enter text")
    hour=int(input("enter hour"))
    min=int(input("Enter minute"))
    pywhatkit.sendwhatmsg(number,msg,hour,min)
