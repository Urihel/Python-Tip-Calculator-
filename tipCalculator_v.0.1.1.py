
class tipCalculator:

    def __init__(self,invoiceAmount,tipPercent):
        self.invoiceAmount = invoiceAmount
        self.tipPercent = tipPercent
        
    def tipFormat(self):
        if self.tipPercent[-1] == '%':
            self.tipPercent = self.tipPercent[:-1]
            x = float(self.invoiceAmount)*(float(self.tipPercent)/100)
            if x.is_integer():
                return int(x)
            elif x != x.is_integer():
                return round(x,2)
   
    
userInput1 = str(input("Please Enter Your Amount :"))
userInput2 = str(input("Please Enter Tip Percentage")) 
tp = tipCalculator(userInput1,userInput2)
print(tp.tipFormat())
