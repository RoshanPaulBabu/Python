def valid(passwd):

    return len(passwd)>=7 and any(i.isupper() for i in passwd) and any(i.islower() for i in passwd) and any(i.isdigit() for i in passwd)


while True:
    passwd = input("Ente your passwd: ")
    
    if valid(passwd):
        print("your passwd is valid")
        break

    else:
        print("Its not valid")
