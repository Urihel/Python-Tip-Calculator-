
#tip calculator

#Where you enter you tab 
x = float(input("Enter Your Bill Amount: "))
#Where you can enter you tip in fomrat 10% or 10
y = str(input("Enter Tip Percent: "))

if y[-1] == '%':
    y = y[:-1]
    print(y)#prints y again but with the % symbol missing this time around 
    y = "." + y #how we add the decimal point to the front of our interger string
    print(y) #shows you how y looks after with the decimal in front 
    print("{:0.2f}".format(x*float(y))) # your tip calculated based on the bill and tip percentage

