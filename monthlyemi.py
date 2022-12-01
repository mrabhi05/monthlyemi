
class Calculations:

    def __init__(self, amount, tax, brokerage, period, amtPossible,expectedROR):
        self.amount = amount
        self.tax = tax
        self.brokerage = brokerage
        self.period = period
        self.amtPossible = amtPossible
        self.expectedROR = expectedROR

    def optionCalc(self, option):
 
        default = "Incorrect Option"
 
        return getattr(self, 'case_' + str(option), lambda: default)()
 
    def case_1(self): # If ROI option is selected;
        o1 =self.amount + tax
        print(self.amtToBeSaved(amount, tax, brokerage, period, amtPossible,expectedROR))
        return "Option 1"
 
    def case_2(self): # If saving amount is selected
        o2 =self.amount + tax
        print(o2)
        return "Option 2"

    def amtToBeSaved(self):
        return ((amount + tax +brokerage)*pow((1+expectedROR),period))/pow((1+expectedROR),period*(period-1))



if __name__ == '__main__':

    amount = float(input("Enter the amount to be saved: "))
    tax = float(input("Enter the tax amount: "))
    brokerage = float(input("Enter the brokerage: "))
    period = float(input("Enter the period: "))
    
    amtPossible = float(input("Enter the amount that you can save: "))
    expectedROR = float(input("Enter the expected rate of return: "))
    expectedROR = expectedROR/100

    calc = Calculations(amount, tax, brokerage, period, amtPossible,expectedROR)

    opt = int(input("Choose any of the following options\n Enter the ROI [Enter 1]\n Enter the saving amount [Enter 2]\n Your option: "))
    if opt == 1: calc.optionCalc(1)
    if opt == 2: calc.optionCalc(2)

    





