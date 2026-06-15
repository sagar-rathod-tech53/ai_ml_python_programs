import os

filename = "myfile.txt"

# Create file and header if not exists
if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("Roll_No\tName\tAge\tClass\tMarks\n")

while True:
    option = input(
        "\n1. Add Data"
        "\n2. Display Data"
        "\n3. Modify Data"
        "\n4. Delete Data"
        "\n5. Exit"
        "\n\nEnter Choice: "
    )

    # CREATE
    if option == "1":
        try:
            role_no = input("Enter Roll No: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            classd = int(input("Enter Class: "))
            marks = int(input("Enter Marks: "))

            if age >= 5 and classd >= 1 and marks >= 0:
                with open(filename, "a") as file:
                    file.write(
                        f"{role_no}\t{name}\t{age}\t{classd}\t{marks}\n"
                    )

                print("Data Added Successfully")

            else:
                print("Invalid Data")

        except ValueError:
            print("Please enter valid numeric values.")

    # READ
    elif option == "2":
        try:
            with open(filename, "r") as file:
                data = file.read()

            print("\nStudent Records")
            print("-" * 50)
            print(data)

        except FileNotFoundError:
            print("File not found.")

    # UPDATE
    elif option == "3":
        roll_no = input("Enter Roll No to Modify: ")

        with open(filename, "r") as file:
            lines = file.readlines()

        found = False

        for i in range(1, len(lines)):  # Skip header
            data = lines[i].strip().split("\t")

            if data[0] == roll_no:
                print("\nCurrent Record:")
                print(lines[i])

                name = input("Enter New Name: ")
                age = input("Enter New Age: ")
                classd = input("Enter New Class: ")
                marks = input("Enter New Marks: ")

                lines[i] = (
                    f"{roll_no}\t{name}\t{age}\t{classd}\t{marks}\n"
                )

                found = True
                break

        if found:
            with open(filename, "w") as file:
                file.writelines(lines)

            print("Record Updated Successfully")
        else:
            print("Roll No not found")

    # DELETE
    elif option == "4":
        roll_no = input("Enter Roll No to Delete: ")

        with open(filename, "r") as file:
            lines = file.readlines()

        found = False
        new_lines = [lines[0]]  # Keep header

        for line in lines[1:]:
            data = line.strip().split("\t")

            if data[0] == roll_no:
                found = True
            else:
                new_lines.append(line)

        if found:
            with open(filename, "w") as file:
                file.writelines(new_lines)

            print("Record Deleted Successfully")
        else:
            print("Roll No not found")

    # EXIT
    elif option == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")