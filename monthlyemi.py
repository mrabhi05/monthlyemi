
class method_switch:
    def day(self, option):
 
        default = "Incorrect Option"
 
        return getattr(self, 'case_' + str(option), lambda: default)()
 
    def case_1(self):
        return "Option 1"
 
    def case_2(self):
        return "Option 2"

if __name__ == '__main__':

    x = input("Enter the amount to be saved: ")
    tax = input("Enter the tax amount: ")
    brokerage = input("Enter the brokerage: ")
    period = input("Enter the period: ")
    option = 1

    print("Enter Option\n1. \n")
    s1 = method_switch()
    print(s1.day(option))






