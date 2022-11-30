
class Calculations:
    def optionCalc(self, option):
 
        default = "Incorrect Option"
 
        return getattr(self, 'case_' + str(option), lambda: default)()
 
    def case_1(self):
        return "Option 1"
 
    def case_2(self):
        return "Option 2"

    def amtToBeSaved(self, x, tax, brokerage, period, amtPossible,ExpectedROR):
        return ((x + tax +brokerage)*pow((1+ExpectedROR),period))/pow((1+ExpectedROR),period*(period-1))
        pass



if __name__ == '__main__':

    x = input("Enter the amount to be saved: ")
    tax = input("Enter the tax amount: ")
    brokerage = input("Enter the brokerage: ")
    period = input("Enter the period: ")
    
    amtPossible = input("Enter the amount that you can save: ")
    ExpectedROR = input("Enter the expected rate of return: ")
    ExpectedROR = ExpectedROR/100





    print("Enter Option\n1. \n")
    s1 = Calculations()
    print(s1.optionCalc(option))






