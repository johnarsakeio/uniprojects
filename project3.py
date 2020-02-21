#a={"goods":{"milk":1.2,"eggs":2.1,"sugar":0.8},"vat":0.24} i suppose another program will be sending something like that to this function?
def price_calc(a):
    x=sum(a["goods"].values())
    x+=x*a["vat"]
    print("total cost is:", x)
    
