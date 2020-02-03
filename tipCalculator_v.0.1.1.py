
#tip calculator

#Where you enter you tab 
x = float(input("Enter Your Bill Amount: "))
#Where you can enter you tip in fomrat 10% or 10
y = str(input("Enter Tip Percent: "))

if y[-1] == '%':
    y = y[:-1]
    print(y)

