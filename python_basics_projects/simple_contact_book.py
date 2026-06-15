scb = []


while True:
    
    option = input("\n\nWhich operation you want to perform \n1 for Add Data \n2 for Display Data \n3 for Modify Data \n4 for Delete Data \n5 for Exit from code \n \n")

    if option == "1":
        while True:
            try:
                name = input("Enter your name: ")
                number = int(input("Enter your number: "))
                email = input("Enter your email: ")
                
                scbs = {"name": name, "number": number, "email": email}
                scb.append(scbs)
                print(f"Name : {name} \nNumber : {number} \nEmail : {email}\n \n")
                print(":::Data added:::\n \n")
                print("\n\n",scb,"\n\n")
                ext_opt = input("You want to exit then click space and enter if you want to add one more data then click enter : ")
                if ext_opt == " ":
                    break
            except (TypeError, ValueError):
                    print("Input invalid")

    elif option == "2":
        print("\n\n")
        i = 0
        while i < len(scb):
            print("Name : ", scb[i]["name"])
            print("Number : ", scb[i]["number"])
            print("Email : ", scb[i]["email"])
            i += 1
        print("\n\n")
    elif option == "3":
        print("\n\n",scb,"\n\n")
        print("\n\n::Check your data in above dataset and update::")
        search_name = input("Enter name to modify: ")

        for contact in scb:
            if contact["name"] == search_name:
                try:
                    contact["number"] = int(input("Enter new number: "))
                    contact["address"] = input("Enter new address: ")
                except (TypeError, ValueError):
                    print("Input invalid")
                print("Data updated")
                break
        print(":::Data update:::")
    elif option == "4":
        print("\n\n",scb,"\n\n")
        print("\n\n::Check your data in above dataset and delete::")
        name = input("Enter name to delete: ")

        for contact in scb:
            if contact["name"] == name:
                scb.remove(contact)
                print("Data deleted")
                break
    elif option == "5":
        break
    else:
        print("Choose the correct option : ")
    
