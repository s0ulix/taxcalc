def prov(inc):
    if(inc<=29590.00):
        return("8.79% [0 .. 29590.00]",(inc*8.79)/100)
    elif(inc<=59180.00):
        return ("14.95% [29590.01 .. 59180.00]", (inc * 14.95) / 100)
    elif(inc<=93000.00):
        return ("16.67% [59180.01 .. 93000.00]", (inc * 16.67) / 100)
    elif (inc <= 150000.00):
        return ("17.50% [93000.01 .. 150000.00]", (inc * 17.50) / 100)
    else:
        return ("21.00% [150000.01 and above]", (inc * 21.00) / 100)


def fed(inc):
    if (inc <= 49020.00):
        return ("15.00% [0 .. 49020.00]", (inc * 15.00) / 100)
    elif (inc <= 98040.00):
        return ("20.50% [49020.01 .. 98040.00]", (inc * 20.50) / 100)
    elif (inc <= 151978.00):
        return ("26.00% [98040.01 .. 151978.00]", (inc * 26.00) / 100)
    elif (inc <= 216511.00):
        return ("29.00% [151978.01 .. 216511.00]", (inc * 29.00) / 100)
    else:
        return ("33.00% [216511.01 and above]", (inc * 33.00) / 100)

def cpp(inc):
    return(min((inc*5.25)/100,2898.00))

def el(inc):
    return(min((inc*1.58)/100,856.36))

def hel(inc):
    if (inc <= 22000.00):
        return(0)
    elif (inc <= 38000.00):
        return(min(((inc-22000.00)*6)/100,300.00))
    elif (inc <= 50000.00):
        return(min(300+(((inc-38000.00)*6)/100),450.00))
    elif (inc <= 74000.00):
        return(min(450+(((inc-50000.00)*25)/100),600.00))
    elif (inc <= 202000.00):
        return(min(600+(((inc-74000.00)*25)/100),750.00))
    else:
        return(min(750+(((inc-202000.00)*6)/100),900.00))

i=float(input("Please enter employee's annual taxable income: CAD($) "))
h=hel(i)
e=el(i)
c=cpp(i)
pr,pt=prov(i)
fr,ft=fed(i)
print("************ Income Value ********\n")
print("Employee's taxable income: CAD($) ", i)
print("Employee's net income: CAD($) ", "{:.2f}".format(i-(h+e+c+pt+ft)))
print("Employee's overall deduction: CAD($) ", "{:.2f}".format(h+e+c+pt+ft),"\n")
print("************** Deduciton *********\n")
print("Employee's CPP: CAD($) ", "{:.2f}".format(c))
print("Employee's EL: CAD($) ", "{:.2f}".format(e))
print("Employee's Health Premium: CAD($) ", "{:.2f}".format(h),"\n")
print("Employee's Provisional tax value: CAD($) ", "{:.2f}".format(pt))
print("Employee's Provisional tax bracket: ", pr,"\n")
print("Employee's Federal tax value: CAD($) ", "{:.2f}".format(ft))
print("Employee's Federal tax bracket: ", fr)
print("Edit by Nishant")
