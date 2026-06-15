class MiniCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        try:
            results = self.num1 / self.num2

            return results
        except ZeroDivisionError:
            print("You Can not divide by 0")
        
        except ValueError:
            print("Value error")
        
        except TypeError:
            print("Invalid input")
        finally:
            print("End the operation")


out = True
while out:


    ext_opt = input("You want to exit then click space and enter if you don't want exit then click enter : ")


    if ext_opt == " ":
        break

    try:
        num1 = int(input("Enter the first Number : "))
        num2 = int(input("Enter the second Number : "))
    
        mini_clt = MiniCalculator(num1, num2)
    
        operator = input("Enter which operation you want to perform : \n+ \n - \n* \n/ \nexit\n")


        if operator == "+":
            print("The Addition is: ",mini_clt.add())
        elif operator == "-":
            print("The Substraction is: ",mini_clt.sub())
        elif operator == "*":
            print("The Multiplication is: ",mini_clt.mul())
        elif operator == "/":
            print("The Divide is: ",mini_clt.div())
        elif operator == "exit":
            break
        else:
            print("Wrong input")
    except (TypeError, ValueError):
                    print("Input invalid")
         
