
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

    x = float(input("Enter the amount to be saved: "))
    tax = float(input("Enter the tax amount: "))
    brokerage = float(input("Enter the brokerage: "))
    period = float(input("Enter the period: "))
    
    amtPossible = float(input("Enter the amount that you can save: "))
    ExpectedROR = float(input("Enter the expected rate of return: "))
    ExpectedROR = ExpectedROR/100

    calc = Calculations()
    print(calc.amtToBeSaved(x, tax, brokerage, period, amtPossible,ExpectedROR))





