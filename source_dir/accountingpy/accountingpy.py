"""
Module : accountingpy.py
Author : Ahmed El-sahooly
Version : 0.0.1
about : AccountingPy Module Provides a set Of Interactive
        Functions to Compute the Most Time Consuming Accounting Formulas
"""

def sl(*x):
    """Straight Line Depreciation Method"""
    cost = float(input("Please Enter the Cost Of The Asset: "))
    rv = float(input("Please Enter Estimated Residual Value Of The Asset: "))
    life = float(input("Please Enter Estimated Useful Life Of The Asset (Years): "))
    r = (float(cost) - float(rv)) / float(life)
    dd = float(cost)-float(rv)
    fg = float(r)/float(12)
    print ">> Your Depreciable Cost is",dd
    print ">> Your Annual Depreciation is ",r
    print ">> Your Monthly Depreciation is",fg
    for i in x:
        lg = float(fg)*float(i)
        print ">> Your Depreciation For",i,"Months is",lg
        
        
def  uop(*val):
    """Straight Line Depreciation Method With Life In Units"""
    cost = float(input("please Enter The Cost Of Asset: "))
    rv = float(input("please Enter Estimated Residual Value Of Asset: "))
    lifeinunits = float(input("please Enter Estimated Life in Units: "))
    rrr = (float(cost) - float(rv)) / float(lifeinunits)
    print ">> Your Depreciation per Unit is ",rrr
    for i in val:
        print ">> Depreciation for ",i,"Units is ",i * rrr
            
            
def ddb():
    """Double Declining Balance Depreciation Method"""
    cost = float(input("Please Enter The Cost Of Asset: "))
    accdepreciation = float(input("Please Enter The Value Of Accumulated Depreciation: "))
    life = float(input("Please Enter Estimated Useful Life Of Asset(Years): "))
    rv = float(input("Please Enter Estimated Residual Value Of Asset: "))
    n = 0
    a = (float(cost)-float(accdepreciation)) * (float(2)/float(life))
    bn = float(a)/float(12)
    print ">> Your Monthly Depreciation For First Year is",bn
    while(n != (life-1)):
        bk = float(cost)
        a = ((float(cost)-float(accdepreciation)) * (float(2)/float(life)))
        cost -= float(a)
        bk -= float(a)
        n += 1
        vvv = float(bk)-float(rv)
        print ">> Your Depreciation For Year No.",n,"is",a
        print ">> Your Book Value After",n,"Years is",bk,"\n"
    print ">> Your Depreciation For Year No.",int(life),"is",vvv
    print ">> Your Book Value After",int(life),"Years is",rv
        
        
def dpr(*val):
    """Depreciation"""
    d = input("For Using Straight Line Method Press 1\nFor Using Units Of Production Method Press 2\nFor Using Double Declining Balance Method Press 3: ")
    if(d == 1):
        from accountingpy import sl
        sl()
    elif(d == 2):
        if(val == 0):
            from accountingpy import uop
            uop()
        elif(val !=0):
            cost = float(input("please Enter The Cost Of Asset: "))
            rv = float(input("please Enter The Residual Value Of Asset: "))
            lifeinunits = float(input("please Enter The Life in Units: "))
            rrr = (float(cost) - float(rv)) / float(lifeinunits)
            print ">> Your Depreciation per Unit is ",rrr
            for i in val:
                print ">> Depreciation for ",i,"Units is ",i * rrr
    elif(d == 3):
        from accountingpy import ddb
        ddb()
        
        
def dpl(*va):
    """Deplation"""
    cost = float(input("Please Enter The Cost Of Resource: "))
    rv = float(input("Please Enter Estimated Residual Value: "))
    totalunits = float(input("Please Enter The Value Of Estimated total units of natural resources: "))
    r = (float(cost) - float(rv)) / float(totalunits)
    print ">> Your Deplation Rate Per Unit is",r,"$"
    for i in va:
        print ">> Your Deplation For ",i,"Units is ",i * r,"$"
        


def ss():
    """Stock Splits Function"""
    a = float(input("Please Enter Original Number Of Outstanding Shares (Stocks): "))
    b = float(input("Please Enter Original Par Value Per Share: "))
    c = float(input("Please Enter Original Market Price Per Share: "))
    d = float(input("Please Enter The Number Of Stock Splits: "))
    e = float(a)*float(d)
    f = float(b)/float(d)
    g = float(c)/float(d)
    print ">> Your Number Of Outstanding Shares After Spliting is",e
    print ">> Your Par Value Per Share After Spliting is",f
    print ">> Your Market Price Per Share After Spliting is",g


       
def nrd():
    """Notes Receivable Discounting"""
    md = float(input("Please Enter Your Receipt Value in Maturity Date: "))
    proceed = float(input("Please Enter the Amount Of Proceed: "))
    time = float(input("Please Enter Number of Months the bank will hold the Note (the discount period): "))
    br = float(input("Please Enter The Bank Discount Rate %: "))
    per = float(br / 100)
    y = (float(md) * float(per)) * float(time / 12)
    gg = float(md - y)
    print ">> Bank Interest Revenue is ",y
    print ">> Seller proceeds from discounting the note receivable is ",gg
    if(gg > proceed):
        io = float(gg) - float(proceed)
        print ">> Your Interest Revenue is ",io
    elif(gg < proceed):
        ff = float(proceed) - float(gg)
        print ">> Your Interest Expence is ",ff
        
        
def ie():
    """Interest Expense Function"""
    ww = float(input("for Short-Term Loan Press 1:\nfor Long-Term Loan Press 2:\nfor Bonds-Payable Press 3: "))
    if(ww == 1):
        e = float(input("Please Enter The Principal Value: "))
        ew = float(input("Please Enter Interest rate %: "))
        ea = float(input("Please Enter Time in Months: "))
        cc = ew/100
        v = (e * cc) * (ea /12)
        l = round(v)
        jj = float(l) + float(e)
        oo =  l / (ea * 30)
        print ">> Your Interest Expense for ",ea,"Months is ",l
        print ">> Total Amount Paid in Maturity Date is ",jj
        print ">> Your Interest Expense Per Day is",oo
    elif(ww == 2):
        spp = float(input("     for Single Payment Loan Press 1\n     for Installment Payment Loan Press 2: "))
        if(spp == 1):
            pv = float(input("Please Enter Principal Value: "))
            ir = float(input("Please Enter Interest rate %: "))
            lp = float(input("Please Enter The Loan Period (Years): "))
            mp = (float(pv) * (float(ir) / float(100))) * (float(1) / float(12))
            yp = float(mp) * float(12)
            semi = float(yp)/float(2)
            ap = float(yp) * float(lp)
            md = float(ap) + float(pv)
            print ">> Your Monthly Interest Expense is ",mp
            print ">> Your Semi-Annual Interest Expense is ",semi
            print ">> Your Interest Expense Per Year is ",yp
            print ">> Total Interest will be Paid is ",ap
            print ">> Principal Value at Maturity Date is ",md
        elif(spp == 2):
            pip = list(input("Please Enter Each Installment Payment: "))
            iir = float(input("Please Enter Interest rate %: "))
            su = sum(pip)
            le = len(pip)
            n = 0
            tie = 0
            while le != 0:
                iex = (float(su)*(float(iir)/float(100)))*(float(1)/float(12))
                sm = float(iex)*float(6)
                an = float(iex)*float(12)
                ey = pip[0 + n]
                dr = float(ey)+float(an)
                n += 1
                le -= 1
                tie += float(an)
                tot = float(su)+float(tie)
                print "Information for Installment no.",n,"with Value Of ",ey
                print ">> Your Monthly Interest Expense is",iex
                print ">> Your Semi-Annual Interest Expense is",sm
                print ">> Your Annual Interest Expense is",an
                print ">> Total Amount Will Be Paid for The Installment is",dr,"\n"
            print ">> Total Interest Expense for The Loan is ",tie
            print ">> Your Total Payment for The Loan is",tot
    elif(ww == 3):
        from accountingpy import bp
        bp()        


def mp(x=0):
    """Mortgages Payment"""
    mb = float(input("Please Enter The Mortgage Value: "))
    interestrate = float(input("Please Enter Interest rate %: "))
    payment = float(input("Please Enter The Monthly Payment Include Interest: "))
    n = 0
    ee = float(mb)
    hh = 0
    while mb >= payment:
        ss = (float(mb)*(float(interestrate)/float(100)))/float(12)
        cc = float(payment)-float(ss)
        mb -= cc
        hh += float(ss)
        dd = float(ee)-float(mb)
        n += 1
        print ">> Your Interest Expense for Month no.",n,"is",ss
        print ">> Your Principal Payment for Month no.",n,"is",cc
        print ">> Mortgage Balance After",n,"Payments","is ",mb,"\n"
        if(n == x):
            break
    print ">> Total Interest Paid After",n,"Months is",hh
    print ">> Total Principal Paid After",n,"Months is",dd
    
    
        
def pv(r=3):
    """Present Value"""
    aa = input("For Using Present Value Press 1\nFor Using Present Value Of Annuity Press 2: ")
    if (aa == 1):
        a = float(input("Please Enter The Future Value: "))
        b = float(input("Please Enter Interest Rate %: "))
        c = float(input("Please Enter The Period Of Investment (Year): "))
        g = 1
        n = 0
        while c != 0:
            d = float(g)/(float(1)+(float(b)/float(100)))
            bb = round(d,r)
            bbb = round(bb,r)
            e = float(g)-float(bbb)
            g -= float(e)
            f = float(a)*float(bb)
            lm = float(a)-float(f)
            n += 1
            c -= 1
        print ">> Your Present Value For",n,"Years is",f
        print ">> Your Earning From Investment is",lm
    elif(aa == 2):
        x = list(input("Please Enter The Future Values: "))
        y = float(input("Please Enter Interest Rate %: "))
        xy = float(input("Please Enter Estimated Residual Value: "))
        a = float(x[-1])+float(xy)
        x[-1] = a
        z = len(x)
        gg = 1
        t = 0
        k = 0
        while z != 0:
            aa = float(gg)/(float(1)+(float(y)/float(100)))
            lm = round(aa,r)
            bb = float(gg)-float(lm)
            bbb = round(bb,r)
            gg -= float(bbb)
            ee = float(x[0 + t])
            hh = float(ee)*float(lm)
            k += float(hh)
            t += 1
            z -= 1
            print ">> Your Present Value Of",ee,"For",t,"Years is",hh
        print ">> Your Total Present Value Of Net Cash Inflows is",k,"\n"
        dd = input("To Calculate Net Present Value Press 1\nTo Exit Press 0: ")
        if(dd == 1):
            ww = float(input("Please Enter The Cost Of Investment: "))
            eer = float(k)-float(ww)
            rre = float(k)/float(ww)
            print ">> Your Net Present Value For",t,"Years is",eer
            print ">> Your Profitability Index is",rre
        elif(dd == 0):
            print "Canceled"


def bp(x=0):
    """Bonds Payable"""
    wow = float(input("for Bonds Without Neither Discount Nor Premium Press 1:\nfor Bonds With Either Discount Or Premium Press 2: "))
    if(wow == 1):
        bv = float(input("Please Enter Bonds-Payable Value: "))
        ir = float(input("Please Enter Interest Rate %: "))
        per = float(input("Please Enter The Period Of Bonds Life(Years): "))
        mb = float(bv)*(float(ir)/float(100))*(float(1)/float(12))
        sa = float(mb)*float(6)
        aa = float(mb)*float(12)
        tie = float(aa)*float(per)
        ta = float(tie)+float(bv)
        print ">> Your Monthly Interest Expense is ",mb
        print ">> Your Semi-Annual Interest Expense is ",sa
        print ">> Your Annual Interest Expense is ",aa,"\n"
        print ">> Total Interest Paid is",tie
        print ">> Total Amount Paid for Bonds-Payable is ",ta
    elif(wow == 2):
        xx = float(input("     for Bonds-Payable With Discount Press 1:\n     for Bonds-Payable With Premium Press 2: "))
        if(xx == 1):
            dl = input("            For Using Straight Line Amortization Method Press 1\n            For Using Effective Interest Amortization Method Press 2: ")
            if(dl == 1):
                aa = float(input("Please Enter The Bonds-Payable Value (Par Value): "))
                a = float(input("Please Enter Bonds-Payable Life(Year): "))
                bb = float(input("Please Enter Stated Interest Rate %: "))
                cc = float(input("Please Enter Discount Rate %: "))
                mie = (float(aa)*(float(bb)/float(100)))*(float(1)/float(12))
                cr = float(aa)*(float(cc)/float(100))
                dv = float(aa)-float(cr)
                md = float(dv)/(float(a)*float(12))
                ti = float(mie)*(float(a)*float(12))
                pmd = float(aa)+float(ti)
                print ">> Your Monthly interest Expense is",mie
                print ">> Your Monthly Discount Amortization is",md
                print ">> Your Total Cash Receipt After Discount is",cr
                print ">> Your Discount Value is",dv
                print ">> Your Total Interest Expense is",ti
                print ">> Your Total Payment In Maturity Date is",pmd
            elif(dl == 2):
                a = float(input("Please Enter The Bonds-Payable Value (Par Value): "))
                c = float(input("Please Enter Stated Interest Rate %: "))
                d = float(input("Please Enter Market Interest Rate %: "))
                e = float(input("Please Enter Discount Rate %: "))
                f = float(a)*(float(e)/float(100)) #actual cash recript
                g = float(a)-float(f) #discount value
                n = 0
                print ">> Your Actual Cash Received (Bond Carrying Amount) is",f
                print ">> Your Discount Value is",g,"\n"                                    
                while g > 0 :
                    i = (float(a)*(float(c)/float(100)))*(float(6)/float(12))
                    j = (float(f)*(float(d)/float(100)))*(float(6)/float(12))
                    k = float(j)-float(i)
                    l = round(k)
                    f += float(l)
                    g -= float(l)
                    n += 1
                    print "Information Related To Payment No.",n
                    print ">> Your Interest Expense According To Stated Interest Rate is",i
                    print ">> Your Interest Expense According To Market Interest Rate is",j
                    print ">> Your Discount Amortization Value is",l
                    print ">> Your Discount Balance After",n,"Payments is",g
                    print ">> Your Bond Carrying Amount After",n,"Payments is",f,"\n"
                    if(n == x):
                        break
        elif(xx == 2):
            dl = input("            For Using Straight Line Amortization Method Press 1\n            For Using Effective Interest Amortization Method Press 2: ")
            if(dl == 1):
                aa = float(input("Please Enter The Bonds-Payable Value (Par Value): "))
                a = float(input("Please Enter Bonds-Payable Life(Year): "))
                bb = float(input("Please Enter Stated Interest Rate %: "))
                cc = float(input("Please Enter Premium Percentage %: "))
                mie = (float(aa)*(float(bb)/float(100)))*(float(1)/float(12))
                cr = float(aa)*(float(cc)/float(100))
                pv = float(cr)-float(aa)
                mp = float(pv)/(float(a)*float(12))
                ti = float(mie)*(float(a)*float(12))
                pmd = float(aa)+float(ti)
                print ">> Your Monthly interest Expense is",mie
                print ">> Your Monthly Premium Amortization is",mp
                print ">> Your Total Cash Receipt After Premium is",cr
                print ">> Your Premium Value is",pv
                print ">> Your Total Interest Expense is",ti
                print ">> Your Total Payment In Maturity Date is",pmd
            elif(dl == 2):
                a = float(input("Please Enter The Bonds-Payable Value (Par Value): "))
                c = float(input("Please Enter Stated Interest Rate %: "))
                d = float(input("Please Enter Market Interest Rate %: "))
                e = float(input("Please Enter Premium Percentage %: "))
                f = float(a)*(float(e)/float(100)) #actual cash recript
                g = float(f)-float(a) #premium value
                n = 0
                print ">> Your Actual Cash Received (Bond Carrying Amount) is",f
                print ">> Your Premium Value is",g,"\n"
                while g > 0 :
                    i = (float(a)*(float(c)/float(100)))*(float(6)/float(12))
                    j = (float(f)*(float(d)/float(100)))*(float(6)/float(12))
                    k = float(i)-float(j)
                    l = round(k)
                    g -= float(l)
                    f -= float(l)
                    n += 1
                    print "Information Related To Payment No.",n
                    print ">> Your Interest Expense According To Stated Interest Rate is",i
                    print ">> Your Interest Expense According To Market Interest Rate is",j
                    print ">> Your Premium Amortization Value is",l
                    print ">> Your Premium Balance After",n,"Payments is",g
                    print ">> Your Bond Carrying Amount After",n,"Payments is",f,"\n"
                    if(n == x):
                        break
            

def pc():
    """Percentage Change"""
    x = float(input("Please Enter The Previous Amount(base amount): "))
    y = float(input("Please Enter The Current Amount: "))
    b = float(y)-float(x)
    d = (float(b)/float(x))*float(100)
    f = (float(100)/float(100))*float(100)
    c = float(f)+float(d)
    if(y > x):
        print ">> Amount With Value Of",x,"Increased by",b
        print ">> Amount Increased by",round(d,1),"% Of Base Amount"
        print ">> Total Percentage Change is",round(c,1),"%"
    elif(y < x):
        print ">> Amount With Value Of",x,"Decreased by",abs(b)
        print ">> Amount Decreased by",round(abs(d),1),"% Of Base Amount"
        print ">> Total Percentage Change is",round(c,1),"%"
        
                                          
def h_analysis():
    """Horizontal Analysis"""
    x = input("Please Enter The Previous Amounts(base amounts): ")
    y = input("Please Enter The Current Amounts: ")
    for i,v in zip(x,y):
        b = float(v)-float(i)
        d = (float(b)/i)*float(100)
        if(v > i):
            print ">> Amount With Value Of",i,"Increased by",b
            print ">> Amount Increased by",round(d,1),"% Of Base Amount\n"
        elif(v < i):
            print ">> Amount With Value Of",i,"Decreased by",abs(b)
            print ">> Amount Decreased by",round(abs(d),1),"% Of Base Amount\n"
            
                                                      
                                                      
def v_analysis():
    """Vertical Analysis"""
    x = float(input("Please Enter The Base Amount: "))
    y = input("Please Enter Items To Calculate Vertical Analysis for: ")
    for i in y:
        d = (float(i)/float(x))*float(100)
        print ">> Item With Value Of",i,"Represent",round(d,1),"% Of Base Amount"
        
        
def wc():
    """Working Capital"""
    a = float(input("Please Enter Current Assets Value: "))
    b = float(input("Please Enter Current Liabilities Value: "))
    c = float(a)-float(b)
    print ">> Your Working Capital is",c
       
        
def cr():
    """Current Ratio"""
    x = float(input("Please Enter Current Assets Value: "))
    y = float(input("Please Enter Current Liabilities Value: "))
    s = float(x)/float(y)
    print ">> Your Current Ratio is",round(s,2)
    

def qr():
    """Quick Ratio"""
    x = float(input("Please Enter Total Current Assets Value: "))
    y = float(input("Please Enter Total Inventory Value: "))
    z = float(input("Please Enter Total Current Liability Value: "))
    s = (float(x)-float(y))/float(z)
    print "Your Quick Ratio(Acid-Test Ratio) is",round(s,2)
                           
                           
def ito():
    """Inventory TurnOver"""
    x = float(input("Please Enter The Cost Of Goods Sold(COGS) Value: "))
    y = float(input("Please Enter Beginning Inventory Value: "))
    z = float(input("Please Enter Ending Inventory Value: "))
    s = float(x)/((float(y)+float(z))/float(2))
    w = float(365)/float(s)
    print ">> Your Inventory TurnOver is",round(s,1)
    print ">> Your Days in Inventory is",round(w),"days"
    
    
def gpp():
    """Gross Profit Percentage"""
    x = float(input("Please Enter Net Sales Value: "))
    y = float(input("Please Enter The Cost Of Goods Sold(COGS) Value: "))
    z = float(x)-float(y)
    a = round(z,3)
    c = (float(a)/float(x))*float(100)
    print ">> Your Gross Profit(Gross Margin) is",a
    print ">> Your Gross Profit Percentage is",round(c,1),"%"
    
    
    
    
def dr():
    """Debt Ratio"""
    x = float(input("Please Enter Total Liabilities Value: "))
    y = float(input("Please Enter Total Assets Value: "))
    s = (float(x)/float(y))*float(100)
    print ">> Your Debt Ratio is",round(s,1),"%"
    
    
def dte():
    """Debt To Equity"""
    x = float(input("Please Enter Total Liabilities Value: "))
    y = float(input("Please Enter Total Equity Value: "))
    s = float(x)/float(y)
    print ">> Your Debt to Equity is",round(s,2)
    
    
def icr():
    """Interest Coverage Ratio"""
    x = float(input("Please Enter Net Income Value: "))
    y = float(input("Please Enter Income Tax Expense Value: "))
    z = float(input("Please Enter Interest Expense Value: "))
    eb = float(x)+float(y)+float(z)
    s = (float(x)+float(y)+float(z))/float(z) 
    print ">> Your Earning Before Interest And Tax (EBIT) is",eb
    print ">> Your Interest-Coverage Ratio is",round(s,2)
    
    
def ros():
    """Return On Sales"""
    x = float(input("Please Enter Net Income Value: "))
    y = float(input("Please Enter Net Sales Value: "))
    s = (float(x)/float(y))*float(100)
    print ">> Your Return On Sales is",round(s,1),"%"
    
    
    
def rta():
    """Return On Total Assets"""
    x = float(input("Please Enter Net Income Value: "))
    y = float(input("Please Enter Interest Expense Value: "))
    z = float(input("Please Enter Beginning Total Assets Value: "))
    w = float(input("Please Enter Ending Total Assets Value: "))
    d = ((float(x)+float(y)) / ((float(z)+float(w)) / float(2))) * float(100)
    print ">> Your Rate of Return on Total Assets is",round(d,1),"%"
    
    
def ato():
    """Asset TurnOver"""
    x = float(input("Please Enter Net Sales Value: "))
    y = float(input("Please Enter Beginning Total Assets Value: "))
    z = float(input("Please Enter Ending Total Assets Value: "))
    d = float(x) / ((float(y)+float(z)) / float(2))
    print ">> Your Asset TurnOver Ratio is",round(d,2)
    
    
def arto():
    """Accounts Receivable TurnOver"""
    x = float(input("Please Enter Net credit sales Value: "))
    y = float(input("Please Enter Beginning Accounts Receivable Value: "))
    z = float(input("Please Enter Ending Accounts Receivable Value: "))
    s = float(x)/((float(y)+float(z))/float(2))
    q = float(365)/float(s)
    print ">> Your Accounts Receivable TurnOver is",round(s,1)
    print ">> Your Days Sales in Receivables is",round(q),"days"
    
    
def roe():
    """Return On Equity"""
    x = float(input("Please Enter Net Income Value: "))
    s = float(input("Please Enter The Value of Preferred dividend Paid: "))
    y = float(input("Please Enter Beginning common stockholders equity Value: "))
    z = float(input("Please Enter Ending common stockholders equity Value: "))
    d = ((float(x)-float(s)) / ((float(y)+float(z)) / float(2))) * float(100)
    print ">> Your Rate of Return on Common Stockholders Equity is",round(d,1),"%"


def per():
    """Price Earnings Ratio"""
    x = float(input("Please Enter Market price per share of common stock: "))
    a = float(input("Please Enter Net Income Value: "))
    b = float(input("Please Enter The Value of Preferred dividend Paid: "))
    c = float(input("Please Enter Number of shares of common stock outstanding: "))
    y = (float(a)-float(b))/float(c)
    s = float(x)/float(y)
    print ">> Your Price/Earnings Ratio is",round(s,2)


def dp():
    """Dividend Payout"""
    x = float(input("Please Enter Annual dividends per share of common stock: "))
    a = float(input("Please Enter Net Income Value: "))
    b = float(input("Please Enter The Value of Preferred dividend Paid: "))
    c = float(input("Please Enter Number of shares of common stock outstanding: "))
    y = (float(a)-float(b))/float(c)
    s = (float(x)/float(y))*float(100)
    print ">> Your Dividend Payout is",s,"%"
    
    
def eps():
    """Earnings Per Share"""
    x = float(input("Please Enter Net Income Value: "))
    s = float(input("Please Enter The Value of Preferred dividend Paid: "))
    y = float(input("Please Enter Number of shares of common stock outstanding: "))
    e = (float(x)-float(s)) / float(y)
    print ">> Your Earnings per Share of Common Stock(EPS) is",round(e,2),"\n"
    b = input("      Press 1 To Calculate Dividend Payout on Common Stock\n      Press 2 to Calculate Price/Earnings Ratio\n      Press 3 to Calculate Dividend Yield on Common Stock\n      Or Press 0 to Exit: ")
    if(b == 1):
        u = float(input("Please Enter Annual dividends per share of common stock: "))
        ggg = (float(u) / float(e)) *float(100)
        print ">> Your Dividend Payout on Common Stock is",round(ggg,2),"%"
    elif(b == 2):
        cc = float(input("Please Enter Market price per share of common stock: "))
        eee = float(cc)/float(e)
        print ">> Your Price/Earnings(P/E) Ratio is",round(eee,2)
    elif(b == 3):
        tt = float(input("Please Enter Annual dividends per share of common stock: "))
        cc = float(input("Please Enter Market price per share of common stock: "))
        xxx = (float(tt)/float(cc)) * float(100)
        print ">> Your Dividend Yield on Common Stock is",round(xxx,2),"%"
    elif(b == 0):
        print "Canceled"
            
            
    
    
    
def dy():
    """Dividend Yield"""
    x = float(input("Please Enter Annual dividends per share of common stock: "))
    y = float(input("Please Enter Market price per share of common stock: "))
    s = (float(x)/float(y))*float(100)
    print ">> Your Dividend Yield is",round(s,1),"%"
    
    
def bvcs():
    """Book Value per Share of Common Stock"""
    a = float(input("Please Enter Total Stockholders Equity Value: "))
    b = float(input("Please Enter Preferred Equity Value: "))
    c = float(input("Please Enter Number of Shares of Common Stock Outstanding: "))
    d = (float(a)-float(b))/float(c)
    print ">> Your Book Value Per Share of Common Stock is",round(d,2)
    
    
    
def r_analysis():
    """Ratio Analysis"""
    a = float(input("Please Enter Net Income(Loss) Value: "))
    b = float(input("Please Enter Net sales Value: "))
    c = float(input("Please Enter Net Credit Sales Value: "))
    d = float(input("Please Enter The Cost Of Goods Sold(COGS) Value: "))
    e = float(input("Please Enter Interest Expense Value: "))
    f = float(input("Please Enter Income Tax Expense Value: "))
    g = float(input("Please Enter Total Current Assets Value: "))
    h = float(input("Please Enter Beginning Accounts Receivable Value: "))
    i = float(input("Please Enter Ending Accounts Receivable Value: "))
    j = float(input("Please Enter Beginning Inventory Value: "))
    k = float(input("Please Enter Ending Inventory Value: "))
    l = float(input("Please Enter Beginning Total Assets Value: "))
    m = float(input("Please Enter Ending Total Assets Value: "))
    n = float(input("Please Enter Total Current Liabilities Value: "))
    o = float(input("Please Enter Total Liabilities Value: "))
    p = float(input("Please Enter Beginning Total Common Equity Value: "))
    q = float(input("Please Enter Ending Total Common Equity Value: "))
    r = float(input("Please Enter Preferred Dividend Value: "))
    s = float(input("Please Enter Annual Dividends Per Share Of Common Stock Value: "))
    t = float(input("Please Enter Number Of Common Shares Outstanding: "))
    u = float(input("Please Enter Market Price Per Share of Common Stock: "))
    uu = float(g)-float(n) #Working capital
    aa = float(g)/float(n)  #current Ratio
    bb = (float(g)-float(k))/float(n)  #Quick Ratio
    cc = float(d)/((float(j)+float(k))/float(2)) #Inventory turnover
    dd = float(365)/float(cc) #Days in inventory
    ee = float(b)-float(d) #gross margin
    ff = (float(ee)/float(b))*float(100) #Gross profit percent
    gg = float(c)/((float(h)+float(i))/float(2)) #Accounts receivable turnover
    hh = float(365)/float(gg) #days in receivable
    ii = (float(o)/float(m))*float(100) #debt ratio
    jj = float(o)/float(q) #debt to equity
    kk = float(a)+float(f)+float(e) #ebit
    ll = float(kk)/float(e) #interest coverage
    mm = (float(a)/float(b))*float(100) #return on sales
    nn = ((float(a)+float(e))/((float(l)+float(m))/float(2)))*float(100) #return on total assets
    oo = float(b)/((float(l)+float(m))/float(2)) #assets turn over
    pp = ((float(a)-float(r))/((float(p)+float(q))/float(2)))*float(100) #return on common equity
    qq = (float(a)-float(r))/float(t) #EPS
    rr = float(u)/float(qq) #Price/Earnings Ratio
    ss = (float(s)/float(u))*float(100) #Dividend Yield
    tt = (float(s)/float(qq))*float(100) #Dividend Payout
    uull = (float(f)/(float(a)-float(f)))*float(100)
    print ">> Your Working Capital is",uu,"\n"
    print ">> Your Current Ratio is",round(aa,2),"\n"
    print ">> Your Quick (Acid-Test) Ratio is",round(bb,2),"\n"
    print ">> Your Inventory TurnOver is",round(cc,1),"\n"
    print ">> Your Days in Inventory is",round(dd),"days \n"
    print ">> Your Gross Profit(Gross Margin) is",ee,"\n"
    print ">> Your Gross Profit Percentage is",round(ff,1),"%\n"
    print ">> Your Accounts Receivable TurnOver is",round(gg,2),"\n"
    print ">> Your Days Sales in Receivables is",round(hh),"\n"
    print ">> Your Debt Ratio is",round(ii,1),"%\n"
    print ">> Your Debt to Equity Ratio is",round(jj,2),"\n"
    print ">> Your Earning Before Interest and Tax is",kk,"\n"
    print ">> Your Interest Coverage Ratio is",round(ll,2),"\n"
    print ">> Your Rate of Return on Net Sales is",round(mm,1),"%\n"
    print ">> Your Rate of Return on Total Assets is",round(nn,1),"%\n"
    print ">> Your Asset TurnOver Ratio is",round(oo,2),"\n"
    print ">> Your Rate of Return on Common Stockholders Equity is",round(pp,1),"%\n"
    print ">> Your Effective Tax Rate is",round(uull,1),"%\n"
    print ">> Your Earnings per Share of Common Stock(EPS) is",round(qq,2),"\n"
    print ">> Your Price/Earnings Ratio is",round(rr,2),"\n"
    print ">> Your Dividend Yield is",round(ss,1),"%\n"
    print ">> Your Dividend Payout is",tt,"%\n"
    
    
    
def uc(*val):
    """Unit Cost"""
    s = input("To Calculate Cost Per Unit For Services Company Press 1\nTo Calculate Cost Per Unit For Merchandising Company Press 2\nTo Calculate Cost Per Unit For Manufacturing Company Press 3: ")
    if(s == 1):
        a = float(input("Please Enter Total Service Costs (Total Expense) Value: "))
        b = float(input("Please Enter Total Number Of Services Provided: "))
        c = float(a)/float(b)
        print ">> Your Cost Per Service is",c
    elif(s == 2):
        d = float(input("Please Enter Beginning Inventory Value: "))
        e = float(input("Please Enter Net Purchases Value: "))
        f = float(input("Please Enter Freight In Value: "))
        g = float(input("Please Enter Ending Inventory Value: "))
        h = (float(d)+float(e)+float(f))-float(g)
        print ">> Your Cost Of Goods Sold is",h
        for i in val:
            dd = float(h)/float(i)
            print ">> Your Cost Per Unit For",i,"Units is",dd
    elif(s == 3):
        i = float(input("Please Enter Beginning Work in Process Inventory Value: "))
        j = float(input("Please Enter Beginning Direct Materials Inventory Value: "))
        k = float(input("Please Enter Purchases of Direct Materials (including freight in): "))
        l = float(input("Please Enter Ending Direct Materials Inventory Value: "))
        m = float(input("Please Enter Direct Labor Cost Value: "))
        n = float(input("Please Enter Indirect Materials Value: "))
        o = float(input("Please Enter Indirect Labor Value: "))
        p = float(input("Please Enter Depreciation Value (plant and equipment): "))
        q = float(input("Please Enter Plant Utilities and Insurance and Property Taxes Value: "))
        r = float(input("Please Enter Ending Work in Process Inventory Value: "))
        ss = (float(j)+float(k))-float(l)  
        t = float(n)+float(o)+float(p)+float(q)  
        u = (float(i)+float(t)+float(ss)+float(m))-float(r)  
        print ">> Your Total Direct Materials Used is",ss
        print ">> Your Total Manufacturing Overhead Cost is",t
        print ">> Your Cost Of Goods Sold is",u
        for ii in val:
            eee = float(u)/float(ii)
            print ">> Your Cost Per Unit For",ii,"Units is",eee
            
            
            
            
def hlm():
    """High Low Method"""
    a = float(input("Please Enter Highest Volume Value: "))
    c = float(input("Please Enter Highest Cost Value: "))
    b = float(input("Please Enter Lowest Volume Value: "))
    d = float(input("Please Enter Lowest Cost Value: "))
    e = float(input("Please Enter Number of Units (To Compute Cost For): "))
    ab = float(a)-float(b)
    cd = float(c)-float(d)
    vr = float(cd)/float(ab)
    fx = float(c)-(float(vr)*float(a))
    mc = float(vr)*float(e)
    mx = float(mc)+float(fx)
    print ">> Your Variable Cost Per Unit is",vr
    print ">> Your Estimated Fixed Cost is",fx
    print ">> Your Estimated Variable Cost is",mc
    print ">> Your Estimated Total Mixed Cost For",e,"Units is",mx
    

def tp():
    """Target Profit"""
    a = float(input("Please Enter Sales Price Per Unit: "))
    b = float(input("Please Enter Variable Cost Per Unit: "))
    c = float(input("Please Enter Your Target Profit: "))
    d = float(input("Please Enter Total Fixed Cost: "))
    e = float(a)-float(b)
    f = (float(d)+float(c))/float(e)
    g = float(e)/float(a)
    gg = float(g)*float(100)
    h = (float(d)+float(c))/float(g)
    print ">> Your Contribution Margin is",e
    print ">> Your Contribution Margin Ratio is",gg,"%"
    print ">> Your Target Profit in Units To Earn",c,"$ is",round(f)
    print ">> Your Target Profit in Dollars To Earn",c,"$ is",h




def mos():
    """Margin of Safety"""
    a = float(input("Please Enter Sales Price Per Unit: "))
    b = float(input("Please Enter Variable Cost Per Unit: "))
    bb = float(input("Please Enter Total Fixed Cost: "))
    c = float(input("Please Enter Expected Sales: "))
    d = float(a)-float(b)
    e = float(bb)/float(d)
    f = float(c)-float(e)
    g = float(f)*float(a)
    print ">> Your Margin of Safety in Units is",f
    print ">> Your Margin of Safety in Dollars is",g


    
def cvp():
    """Cost Volume Profit Analysis"""
    c = float(input("Please Enter Total Fixed Costs Value: "))
    a = float(input("Please Enter Sale Price Per Unit: "))
    b = float(input("Please Enter Variable Cost Per Unit: "))
    ccm = float(a)-float(b)
    cuu = float(c)/float(ccm)
    ccmr = (float(ccm)/float(a))*float(100)
    cda = float(c)/(float(ccmr)/float(100))
    print ">> Your Contribution Margin is",ccm
    print ">> Your Breakeven Sales in Units is",round(cuu)
    print ">> Your Contribution Margin Ratio is",ccmr,"%"
    print ">> Your Breakeven Sales in Dollars is",cda,"\n"
    qq = input("       Press 1 To Compute Target Profit\n       Press 2 To Compute Margin of Safety\n       Press 3 To Perform Sensitivity Analysis\n       Or Press 0 To Exit: ")
    if(qq == 1):
        dds = float(input("Please Enter Your Target Profit: "))
        xxx = (float(c)+float(dds))/float(ccm)
        xxxx = (float(c)+float(dds))/(float(ccmr)/float(100))
        print ">> Your Target Profit in Units To Earn",dds,"$ is",round(xxx)
        print ">> Your Target Profit in Dollars To Earn",dds,"$ is",xxxx
    elif(qq == 0):
        print "Canceled"
    elif(qq == 2):
        xc = float(input("Please Enter Expected Sales in Units: "))
        zzz = float(xc)-float(cuu)
        zzzz = float(zzz)*float(a)
        print ">> Your Margin of Safety in Units is",round(zzz)
        print ">> Your Margin of Safety in Dollars is",zzzz
    elif(qq == 3):
        i = input("Please Enter Total Fixed Costs Value: ")
        o = input("Please Enter Sale Price Per Unit: ")
        p = input("Please Enter Variable Cost Per Unit: ")
        n = 0
        for x,y,z in zip(i,o,p):
            cm = float(y)-float(z)
            uu = float(x)/float(cm)
            cmr = (float(cm)/float(y))*float(100)
            da = float(x)/(float(cmr)/float(100))
            n += 1
            print "Your Results in Case",int(n),"is :"
            print ">> Your Contribution Margin is",cm
            print ">> Your Breakeven Sales in Units is",round(uu)
            print ">> Your Contribution Margin Ratio is",cmr,"%"
            print ">> Your Breakeven Sales in Dollars is",da,"\n"
            if(cm > ccm):
                a = float(cm)-float(ccm)
                print ">> Your Contribution Margin Increased by",a
            elif(ccm > cm):
                a = float(ccm)-float(cm)
                print ">> Your Contribution Margin Decreased by",a
            if(uu > cuu):
                b = float(uu)-float(cuu)
                print ">> Your Breakeven Sales in Units Increased by",round(b)
            elif(cuu > uu):
                b = float(cuu)-float(uu)
                print ">> Your Breakeven Sales in Units Decreased by",round(b)
            if(cmr > ccmr):
                c = float(cmr)-float(ccmr)
                print ">> Your Contribution Margin Ratio Increased by",c,"%"
            elif(ccmr > cmr):
                c = float(ccmr)-float(cmr)
                print ">> Your Contribution Margin Ratio Decreased by",c,"%"
            if(da > cda):
                d = float(da)-float(cda)
                print ">> Your Breakeven Sales in Dollars Increased by",d
            elif(cda > da):
                d = float(cda)-float(da)
                print ">> Your Breakeven Sales in Dollars Decreased by",d,"\n"
            
            
            
def pp():
    """Payback Period"""
    a = input("For Payback with Equal Annual Net Cash Inflows Press 1\nFor Payback with Unequal Net Cash Inflows Press 2: ")
    if (a == 1):
        b = float(input("Please Enter Total Amount Invested: "))
        c = float(input("Please Enter Expected Annual Net Cash Inflow: "))
        d = float(input("Please Enter Investment Useful Life (Years): "))
        e = (float(c)*float(d))-float(b)
        f = float(b)/float(c)
        print ">> Your Payback Period is",f,"Years"
        print ">> Total Amount Remaining After Payback Period is",e,"(Residual Value Not Included)"
    elif(a == 2):
        b = float(input("Please Enter Total Amount Invested: "))
        c = list(input("Please Enter Expected Annual Net Cash Inflow: "))
        n = 0
        t = 0
        ss = sum(c)
        am = float(ss)-float(b)
        if(ss < b):
            print ">> Your Loss On Investment is",abs(am)
        elif(ss > b):
            while t <= b:
                e = c[0 + n]
                t += float(e)
                n += 1
        gg = c[n - 1]
        ii = (float(t)-float(b))/float(gg)
        ccc = float(n)-float(ii)
        print ">> Your Payback Period is",ccc,"Years"
        print ">> Total Amount Remaining After Payback Period is",am
        
        
        
def ror():
    """Rate Of Return"""
    a = input("For Asset with Equal Annual Net Cash Inflows Press 1\nFor Asset with Unequal Net Cash Inflows Press 2: ")
    if(a == 1):
        b = float(input("Please Enter Annual Cash Inflows For The Asset: "))
        c = float(input("Please Enter Asset Useful Life (Years): "))
        d = float(input("Please Enter Total Depreciation During Operating Life Of Asset: "))
        e = float(input("Please Enter Any Asset Salvage Value: "))
        avo = ((float(b)*float(c))-(float(d)-float(e)))/float(c)
        avi = (float(d)+float(e))/float(2)
        ror = (float(avo)/float(avi))*float(100)
        print ">> Your Average Annual Operating Income From an Asset is",avo
        print ">> Your Average Amount Invested in an Asset is",avi
        print ">> Your Rate Of Return (ROR) is",ror,"%"
    elif(a == 2):
        b = list(input("Please Enter Annual Cash Inflows For The Asset: "))
        d = float(input("Please Enter Total Depreciation During Operating Life Of Asset: "))
        e = float(input("Please Enter Any Asset Salvage Value: "))
        f = sum(b)
        c = len(b)
        g = (float(f)-(float(d)-float(e)))/float(c)
        h = (float(d)+float(e))/float(2)
        ror = (float(g)/float(h))*float(100)
        print ">> Your Average Annual Operating Income From an Asset is",g
        print ">> Your Average Amount Invested in an Asset is",h
        print ">> Your Rate Of Return (ROR) is",ror,"%"
        
                                      
def ci():
    """Compound Interest"""
    ffg = input("If Interest Added Monthly Press 1\nIf Interest Added Annually Press 2: ")
    if(ffg == 1):
        a = float(input("Pleae Enter The Principal Value: "))
        b = float(input("Pleae Enter Interest Rate %: "))
        c = float(input("Please Enter The Loan Period (Months): "))
        t = 0
        n = 0
        g = a
        while c != 0:
            ie = (float(a) * (float(b)/float(100))) * (float(1)/float(12))
            a += float(ie)
            t += float(ie)
            n += 1
            c -= 1
            dd = float(g)+float(t)
            print ">> Your Interest Expense For Month No.",n,"is",ie
        print ">> Your Total Interest Expense For",n,"Months is",t
        print ">> Your Total Payment in Maturity Date is",dd
    elif(ffg == 2):
        a = float(input("Pleae Enter The Principal Value: "))
        b = float(input("Pleae Enter Interest Rate %: "))
        c = float(input("Please Enter The Loan Period (Years): "))
        t = 0
        n = 0
        g = a
        while c != 0:
            ie = float(a) * (float(b)/float(100)) 
            a += float(ie)
            t += float(ie)
            n += 1
            c -= 1
            dd = float(g)+float(t)
            print ">> Your Interest Expense For Year No.",n,"is",ie
        print ">> Your Total Interest Expense For",n,"Years is",t
        print ">> Your Total Payment in Maturity Date is",dd
        
        
        
        
def pvr():
    """Price Variance"""
    a = float(input("Please Enter Your Actual Price: "))
    b = float(input("Please Enter Your Standard Price: "))
    c = float(input("Please Enter Actual Quantity: "))
    d = float(a)-float(b)
    e = float(d)*float(c)
    print ">> Your Change In Price is",d
    print ">> Your Price Variance is",e
    
    
    
def evr():
    """Efficiency Variance"""
    a = float(input("Please Enter Your Actual Quantity: "))
    b = float(input("Please Enter Your Standard Quantity: "))
    c = float(input("Please Enter Your Standard Price: "))
    d = float(a)-float(b)
    e = float(d)*float(c)
    print ">> Your Change In Quantity is",d
    print ">> Your Efficiency Variance is",e
    
    
    
def pm():
    """Profit Margin"""
    a = float(input("Please Enter Operating Income Value: "))
    b = float(input("Please Enter Total Sales Value: "))
    c = (float(a)/float(b))*float(100)
    print ">> Your Profit Margin is",c,"%"
    
    
    
def roi():
    """Return On Investment"""
    a = float(input("Please Enter Operating Income Value: "))
    b = float(input("Please Enter Beginning Total Assets Value: "))
    c = float(input("Please Enter Ending Total Assets Value: "))
    d = (float(a)/((float(b)+float(c))/float(2)))*float(100)
    print ">> Your Return on Investment (ROI) is",d,"% \n"
    e = input("To Calculate Profit Margin And Asset TurnOver Press 1\n To Exit Press 0: ")
    if(e == 1):
        f = float(input("Please Enter Total Sales Value: "))
        i = (float(b)+float(c))/float(2)
        g = (float(a)/float(f))*float(100)
        h = float(f)/float(i)
        print ">> Your Profit Margin is",g,"%"
        print ">> Your Asset TurnOver is",h
        
        
        
def ri():
    """Residual Income"""
    a = float(input("Please Enter Operating Income Value: "))
    b = float(input("Please Enter Your Target Rate Of Return %: "))
    c = float(input("Please Enter Beginning Total Assets Value: "))
    d = float(input("Please Enter Ending Total Assets Value: "))
    e = (float(b)/float(100))*((float(c)+float(d))/float(2))
    f = float(a)-float(e)
    print ">> Your Minimum Acceptable Operating Income is",e
    print ">> Your Residual Income (RI) is",f
                                   
                                   
                                   
def etr():
    """Effective Tax Rate"""
    b = float(input("Please Enter Net Income Value: "))
    a = float(input("Please Enter Income Tax Expense: "))
    c = float(b)+float(a)
    d = (float(a)/float(c))*float(100)
    e = float(100)-float(d)
    f = float(c)*(float(e)/float(100))
    print ">> Your Pre Tax Income is",c
    print ">> Your Effective Tax Rate is",round(d,1),"%"
    print ">> Your After-Tax Operating Income is",f
    
    
    
def eva():
    """Economic Value Added"""
    a = float(input("Please Enter After Tax Operating Income: "))
    b = float(input("Please Enter Current Liabilities Value: "))
    c = float(input("Please Enter Weighted Average Cost Of Capital (minimum rate of return required) %: "))
    d = float(input("Please Enter Beginning Total Assets Value: "))
    e = float(input("Please Enter Ending Total Assets Value: "))
    f = float(a)-((((float(d)+float(e))/float(2))-float(b))*(float(c)/float(100)))
    print ">> Your Economic Value Added (EVA) is",f
                                        
                                        
def straight_line(*x):
    """Straight Line Depreciation Method"""
    cost = float(input("Please Enter the Cost Of The Asset: "))
    rv = float(input("Please Enter Estimated Residual Value Of The Asset: "))
    life = float(input("Please Enter Estimated Useful Life Of The Asset (Years): "))
    r = (float(cost) - float(rv)) / float(life)
    dd = float(cost)-float(rv)
    fg = float(r)/float(12)
    print ">> Your Depreciable Cost is",dd
    print ">> Your Annual Depreciation is ",r
    print ">> Your Monthly Depreciation is",fg
    for i in x:
        lg = float(fg)*float(i)
        print ">> Your Depreciation For",i,"Months is",lg
        
        
def  units_of_production(*val):
    """Straight Line Depreciation Method With Life In Units"""
    cost = float(input("please Enter The Cost Of Asset: "))
    rv = float(input("please Enter Estimated Residual Value Of Asset: "))
    lifeinunits = float(input("please Enter Estimated Life in Units: "))
    rrr = (float(cost) - float(rv)) / float(lifeinunits)
    print ">> Your Depreciation per Unit is ",rrr
    for i in val:
        print ">> Depreciation for ",i,"Units is ",i * rrr
            
            
def double_declining_balance():
    """Double Declining Balance Depreciation Method"""
    cost = float(input("Please Enter The Cost Of Asset: "))
    accdepreciation = float(input("Please Enter The Value Of Accumulated Depreciation: "))
    life = float(input("Please Enter Estimated Useful Life Of Asset(Years): "))
    rv = float(input("Please Enter Estimated Residual Value Of Asset: "))
    n = 0
    a = (float(cost)-float(accdepreciation)) * (float(2)/float(life))
    bn = float(a)/float(12)
    print ">> Your Monthly Depreciation For First Year is",bn
    while(n != (life-1)):
        bk = float(cost)
        a = ((float(cost)-float(accdepreciation)) * (float(2)/float(life)))
        cost -= float(a)
        bk -= float(a)
        n += 1
        vvv = float(bk)-float(rv)
        print ">> Your Depreciation For Year No.",n,"is",a
        print ">> Your Book Value After",n,"Years is",bk,"\n"
    print ">> Your Depreciation For Year No.",int(life),"is",vvv
    print ">> Your Book Value After",int(life),"Years is",rv
        
        
def depreciation(*val):
    """Depreciation"""
    d = input("For Using Straight Line Method Press 1\nFor Using Units Of Production Method Press 2\nFor Using Double Declining Balance Method Press 3: ")
    if(d == 1):
        from accountingpy import sl
        sl()
    elif(d == 2):
        if(val == 0):
            from accountingpy import uop
            uop()
        elif(val !=0):
            cost = float(input("please Enter The Cost Of Asset: "))
            rv = float(input("please Enter The Residual Value Of Asset: "))
            lifeinunits = float(input("please Enter The Life in Units: "))
            rrr = (float(cost) - float(rv)) / float(lifeinunits)
            print ">> Your Depreciation per Unit is ",rrr
            for i in val:
                print ">> Depreciation for ",i,"Units is ",i * rrr
    elif(d == 3):
        from accountingpy import ddb
        ddb()
        
        
def deplation(*va):
    """Deplation"""
    cost = float(input("Please Enter The Cost Of Resource: "))
    rv = float(input("Please Enter Estimated Residual Value: "))
    totalunits = float(input("Please Enter The Value Of Estimated total units of natural resources: "))
    r = (float(cost) - float(rv)) / float(totalunits)
    print ">> Your Deplation Rate Per Unit is",r,"$"
    for i in va:
        print ">> Your Deplation For ",i,"Units is ",i * r,"$"
        


def stock_splits():
    """Stock Splits Function"""
    a = float(input("Please Enter Original Number Of Outstanding Shares (Stocks): "))
    b = float(input("Please Enter Original Par Value Per Share: "))
    c = float(input("Please Enter Original Market Price Per Share: "))
    d = float(input("Please Enter The Number Of Stock Splits: "))
    e = float(a)*float(d)
    f = float(b)/float(d)
    g = float(c)/float(d)
    print ">> Your Number Of Outstanding Shares After Spliting is",e
    print ">> Your Par Value Per Share After Spliting is",f
    print ">> Your Market Price Per Share After Spliting is",g


       
def notes_receivable_discounting():
    """Notes Receivable Discounting"""
    md = float(input("Please Enter Your Receipt Value in Maturity Date: "))
    proceed = float(input("Please Enter the Amount Of Proceed: "))
    time = float(input("Please Enter Number of Months the bank will hold the Note (the discount period): "))
    br = float(input("Please Enter The Bank Discount Rate %: "))
    per = float(br / 100)
    y = (float(md) * float(per)) * float(time / 12)
    gg = float(md - y)
    print ">> Bank Interest Revenue is ",y
    print ">> Seller proceeds from discounting the note receivable is ",gg
    if(gg > proceed):
        io = float(gg) - float(proceed)
        print ">> Your Interest Revenue is ",io
    elif(gg < proceed):
        ff = float(proceed) - float(gg)
        print ">> Your Interest Expence is ",ff
        
        
def interest_expense():
    """Interest Expense Function"""
    ww = float(input("for Short-Term Loan Press 1:\nfor Long-Term Loan Press 2:\nfor Bonds-Payable Press 3: "))
    if(ww == 1):
        e = float(input("Please Enter The Principal Value: "))
        ew = float(input("Please Enter Interest rate %: "))
        ea = float(input("Please Enter Time in Months: "))
        cc = ew/100
        v = (e * cc) * (ea /12)
        l = round(v)
        jj = float(l) + float(e)
        oo =  l / (ea * 30)
        print ">> Your Interest Expense for ",ea,"Months is ",l
        print ">> Total Amount Paid in Maturity Date is ",jj
        print ">> Your Interest Expense Per Day is",oo
    elif(ww == 2):
        spp = float(input("     for Single Payment Loan Press 1\n     for Installment Payment Loan Press 2: "))
        if(spp == 1):
            pv = float(input("Please Enter Principal Value: "))
            ir = float(input("Please Enter Interest rate %: "))
            lp = float(input("Please Enter The Loan Period (Years): "))
            mp = (float(pv) * (float(ir) / float(100))) * (float(1) / float(12))
            yp = float(mp) * float(12)
            semi = float(yp)/float(2)
            ap = float(yp) * float(lp)
            md = float(ap) + float(pv)
            print ">> Your Monthly Interest Expense is ",mp
            print ">> Your Semi-Annual Interest Expense is ",semi
            print ">> Your Interest Expense Per Year is ",yp
            print ">> Total Interest will be Paid is ",ap
            print ">> Principal Value at Maturity Date is ",md
        elif(spp == 2):
            pip = list(input("Please Enter Each Installment Payment: "))
            iir = float(input("Please Enter Interest rate %: "))
            su = sum(pip)
            le = len(pip)
            n = 0
            tie = 0
            while le != 0:
                iex = (float(su)*(float(iir)/float(100)))*(float(1)/float(12))
                sm = float(iex)*float(6)
                an = float(iex)*float(12)
                ey = pip[0 + n]
                dr = float(ey)+float(an)
                n += 1
                le -= 1
                tie += float(an)
                tot = float(su)+float(tie)
                print "Information for Installment no.",n,"with Value Of ",ey
                print ">> Your Monthly Interest Expense is",iex
                print ">> Your Semi-Annual Interest Expense is",sm
                print ">> Your Annual Interest Expense is",an
                print ">> Total Amount Will Be Paid for The Installment is",dr,"\n"
            print ">> Total Interest Expense for The Loan is ",tie
            print ">> Your Total Payment for The Loan is",tot
    elif(ww == 3):
        from accountingpy import bp
        bp()        


def mortgages_payment(x=0):
    """Mortgages Payment"""
    mb = float(input("Please Enter The Mortgage Value: "))
    interestrate = float(input("Please Enter Interest rate %: "))
    payment = float(input("Please Enter The Monthly Payment Include Interest: "))
    n = 0
    ee = float(mb)
    hh = 0
    while mb >= payment:
        ss = (float(mb)*(float(interestrate)/float(100)))/float(12)
        cc = float(payment)-float(ss)
        mb -= cc
        hh += float(ss)
        dd = float(ee)-float(mb)
        n += 1
        print ">> Your Interest Expense for Month no.",n,"is",ss
        print ">> Your Principal Payment for Month no.",n,"is",cc
        print ">> Mortgage Balance After",n,"Payments","is ",mb,"\n"
        if(n == x):
            break
    print ">> Total Interest Paid After",n,"Months is",hh
    print ">> Total Principal Paid After",n,"Months is",dd
    
    
        
def present_value(r=3):
    """Present Value"""
    aa = input("For Using Present Value Press 1\nFor Using Present Value Of Annuity Press 2: ")
    if (aa == 1):
        a = float(input("Please Enter The Future Value: "))
        b = float(input("Please Enter Interest Rate %: "))
        c = float(input("Please Enter The Period Of Investment (Year): "))
        g = 1
        n = 0
        while c != 0:
            d = float(g)/(float(1)+(float(b)/float(100)))
            bb = round(d,r)
            bbb = round(bb,r)
            e = float(g)-float(bbb)
            g -= float(e)
            f = float(a)*float(bb)
            lm = float(a)-float(f)
            n += 1
            c -= 1
        print ">> Your Present Value For",n,"Years is",f
        print ">> Your Earning From Investment is",lm
    elif(aa == 2):
        x = list(input("Please Enter The Future Values: "))
        y = float(input("Please Enter Interest Rate %: "))
        xy = float(input("Please Enter Estimated Residual Value: "))
        a = float(x[-1])+float(xy)
        x[-1] = a
        z = len(x)
        gg = 1
        t = 0
        k = 0
        while z != 0:
            aa = float(gg)/(float(1)+(float(y)/float(100)))
            lm = round(aa,r)
            bb = float(gg)-float(lm)
            bbb = round(bb,r)
            gg -= float(bbb)
            ee = float(x[0 + t])
            hh = float(ee)*float(lm)
            k += float(hh)
            t += 1
            z -= 1
            print ">> Your Present Value Of",ee,"For",t,"Years is",hh
        print ">> Your Total Present Value Of Net Cash Inflows is",k,"\n"
        dd = input("To Calculate Net Present Value Press 1\nTo Exit Press 0: ")
        if(dd == 1):
            ww = float(input("Please Enter The Cost Of Investment: "))
            eer = float(k)-float(ww)
            rre = float(k)/float(ww)
            print ">> Your Net Present Value For",t,"Years is",eer
            print ">> Your Profitability Index is",rre
        elif(dd == 0):
            print "Canceled"


def bonds_payable(x=0):
    """Bonds Payable"""
    wow = float(input("for Bonds Without Neither Discount Nor Premium Press 1:\nfor Bonds With Either Discount Or Premium Press 2: "))
    if(wow == 1):
        bv = float(input("Please Enter Bonds-Payable Value: "))
        ir = float(input("Please Enter Interest Rate %: "))
        per = float(input("Please Enter The Period Of Bonds Life(Years): "))
        mb = float(bv)*(float(ir)/float(100))*(float(1)/float(12))
        sa = float(mb)*float(6)
        aa = float(mb)*float(12)
        tie = float(aa)*float(per)
        ta = float(tie)+float(bv)
        print ">> Your Monthly Interest Expense is ",mb
        print ">> Your Semi-Annual Interest Expense is ",sa
        print ">> Your Annual Interest Expense is ",aa,"\n"
        print ">> Total Interest Paid is",tie
        print ">> Total Amount Paid for Bonds-Payable is ",ta
    elif(wow == 2):
        xx = float(input("     for Bonds-Payable With Discount Press 1:\n     for Bonds-Payable With Premium Press 2: "))
        if(xx == 1):
            dl = input("            For Using Straight Line Amortization Method Press 1\n            For Using Effective Interest Amortization Method Press 2: ")
            if(dl == 1):
                aa = float(input("Please Enter The Bonds-Payable Value (Par Value): "))
                a = float(input("Please Enter Bonds-Payable Life(Year): "))
                bb = float(input("Please Enter Stated Interest Rate %: "))
                cc = float(input("Please Enter Discount Rate %: "))
                mie = (float(aa)*(float(bb)/float(100)))*(float(1)/float(12))
                cr = float(aa)*(float(cc)/float(100))
                dv = float(aa)-float(cr)
                md = float(dv)/(float(a)*float(12))
                ti = float(mie)*(float(a)*float(12))
                pmd = float(aa)+float(ti)
                print ">> Your Monthly interest Expense is",mie
                print ">> Your Monthly Discount Amortization is",md
                print ">> Your Total Cash Receipt After Discount is",cr
                print ">> Your Discount Value is",dv
                print ">> Your Total Interest Expense is",ti
                print ">> Your Total Payment In Maturity Date is",pmd
            elif(dl == 2):
                a = float(input("Please Enter The Bonds-Payable Value (Par Value): "))
                c = float(input("Please Enter Stated Interest Rate %: "))
                d = float(input("Please Enter Market Interest Rate %: "))
                e = float(input("Please Enter Discount Rate %: "))
                f = float(a)*(float(e)/float(100)) #actual cash recript
                g = float(a)-float(f) #discount value
                n = 0
                print ">> Your Actual Cash Received (Bond Carrying Amount) is",f
                print ">> Your Discount Value is",g,"\n"                                    
                while g > 0 :
                    i = (float(a)*(float(c)/float(100)))*(float(6)/float(12))
                    j = (float(f)*(float(d)/float(100)))*(float(6)/float(12))
                    k = float(j)-float(i)
                    l = round(k)
                    f += float(l)
                    g -= float(l)
                    n += 1
                    print "Information Related To Payment No.",n
                    print ">> Your Interest Expense According To Stated Interest Rate is",i
                    print ">> Your Interest Expense According To Market Interest Rate is",j
                    print ">> Your Discount Amortization Value is",l
                    print ">> Your Discount Balance After",n,"Payments is",g
                    print ">> Your Bond Carrying Amount After",n,"Payments is",f,"\n"
                    if(n == x):
                        break
        elif(xx == 2):
            dl = input("            For Using Straight Line Amortization Method Press 1\n            For Using Effective Interest Amortization Method Press 2: ")
            if(dl == 1):
                aa = float(input("Please Enter The Bonds-Payable Value (Par Value): "))
                a = float(input("Please Enter Bonds-Payable Life(Year): "))
                bb = float(input("Please Enter Stated Interest Rate %: "))
                cc = float(input("Please Enter Premium Percentage %: "))
                mie = (float(aa)*(float(bb)/float(100)))*(float(1)/float(12))
                cr = float(aa)*(float(cc)/float(100))
                pv = float(cr)-float(aa)
                mp = float(pv)/(float(a)*float(12))
                ti = float(mie)*(float(a)*float(12))
                pmd = float(aa)+float(ti)
                print ">> Your Monthly interest Expense is",mie
                print ">> Your Monthly Premium Amortization is",mp
                print ">> Your Total Cash Receipt After Premium is",cr
                print ">> Your Premium Value is",pv
                print ">> Your Total Interest Expense is",ti
                print ">> Your Total Payment In Maturity Date is",pmd
            elif(dl == 2):
                a = float(input("Please Enter The Bonds-Payable Value (Par Value): "))
                c = float(input("Please Enter Stated Interest Rate %: "))
                d = float(input("Please Enter Market Interest Rate %: "))
                e = float(input("Please Enter Premium Percentage %: "))
                f = float(a)*(float(e)/float(100)) #actual cash recript
                g = float(f)-float(a) #premium value
                n = 0
                print ">> Your Actual Cash Received (Bond Carrying Amount) is",f
                print ">> Your Premium Value is",g,"\n"
                while g > 0 :
                    i = (float(a)*(float(c)/float(100)))*(float(6)/float(12))
                    j = (float(f)*(float(d)/float(100)))*(float(6)/float(12))
                    k = float(i)-float(j)
                    l = round(k)
                    g -= float(l)
                    f -= float(l)
                    n += 1
                    print "Information Related To Payment No.",n
                    print ">> Your Interest Expense According To Stated Interest Rate is",i
                    print ">> Your Interest Expense According To Market Interest Rate is",j
                    print ">> Your Premium Amortization Value is",l
                    print ">> Your Premium Balance After",n,"Payments is",g
                    print ">> Your Bond Carrying Amount After",n,"Payments is",f,"\n"
                    if(n == x):
                        break
            

def percentage_change():
    """Percentage Change"""
    x = float(input("Please Enter The Previous Amount(base amount): "))
    y = float(input("Please Enter The Current Amount: "))
    b = float(y)-float(x)
    d = (float(b)/float(x))*float(100)
    f = (float(100)/float(100))*float(100)
    c = float(f)+float(d)
    if(y > x):
        print ">> Amount With Value Of",x,"Increased by",b
        print ">> Amount Increased by",round(d,1),"% Of Base Amount"
        print ">> Total Percentage Change is",round(c,1),"%"
    elif(y < x):
        print ">> Amount With Value Of",x,"Decreased by",abs(b)
        print ">> Amount Decreased by",round(abs(d),1),"% Of Base Amount"
        print ">> Total Percentage Change is",round(c,1),"%"
        
                                          
def horizontal_analysis():
    """Horizontal Analysis"""
    x = input("Please Enter The Previous Amounts(base amounts): ")
    y = input("Please Enter The Current Amounts: ")
    for i,v in zip(x,y):
        b = float(v)-float(i)
        d = (float(b)/i)*float(100)
        if(v > i):
            print ">> Amount With Value Of",i,"Increased by",b
            print ">> Amount Increased by",round(d,1),"% Of Base Amount\n"
        elif(v < i):
            print ">> Amount With Value Of",i,"Decreased by",abs(b)
            print ">> Amount Decreased by",round(abs(d),1),"% Of Base Amount\n"
            
                                                      
                                                      
def vertical_analysis():
    """Vertical Analysis"""
    x = float(input("Please Enter The Base Amount: "))
    y = input("Please Enter Items To Calculate Vertical Analysis for: ")
    for i in y:
        d = (float(i)/float(x))*float(100)
        print ">> Item With Value Of",i,"Represent",round(d,1),"% Of Base Amount"
        
        
def working_capital():
    """Working Capital"""
    a = float(input("Please Enter Current Assets Value: "))
    b = float(input("Please Enter Current Liabilities Value: "))
    c = float(a)-float(b)
    print ">> Your Working Capital is",c
       
        
def current_ratio():
    """Current Ratio"""
    x = float(input("Please Enter Current Assets Value: "))
    y = float(input("Please Enter Current Liabilities Value: "))
    s = float(x)/float(y)
    print ">> Your Current Ratio is",round(s,2)
    

def quick_ratio():
    """Quick Ratio"""
    x = float(input("Please Enter Total Current Assets Value: "))
    y = float(input("Please Enter Total Inventory Value: "))
    z = float(input("Please Enter Total Current Liability Value: "))
    s = (float(x)-float(y))/float(z)
    print "Your Quick Ratio(Acid-Test Ratio) is",round(s,2)
                           
                           
def inventory_turnover():
    """Inventory TurnOver"""
    x = float(input("Please Enter The Cost Of Goods Sold(COGS) Value: "))
    y = float(input("Please Enter Beginning Inventory Value: "))
    z = float(input("Please Enter Ending Inventory Value: "))
    s = float(x)/((float(y)+float(z))/float(2))
    w = float(365)/float(s)
    print ">> Your Inventory TurnOver is",round(s,1)
    print ">> Your Days in Inventory is",round(w),"days"
    
    
def gross_profit_percentage():
    """Gross Profit Percentage"""
    x = float(input("Please Enter Net Sales Value: "))
    y = float(input("Please Enter The Cost Of Goods Sold(COGS) Value: "))
    z = float(x)-float(y)
    a = round(z,3)
    c = (float(a)/float(x))*float(100)
    print ">> Your Gross Profit(Gross Margin) is",a
    print ">> Your Gross Profit Percentage is",round(c,1),"%"
    
    
    
    
def debt_ratio():
    """Debt Ratio"""
    x = float(input("Please Enter Total Liabilities Value: "))
    y = float(input("Please Enter Total Assets Value: "))
    s = (float(x)/float(y))*float(100)
    print ">> Your Debt Ratio is",round(s,1),"%"
    
    
def debt_to_equity():
    """Debt To Equity"""
    x = float(input("Please Enter Total Liabilities Value: "))
    y = float(input("Please Enter Total Equity Value: "))
    s = float(x)/float(y)
    print ">> Your Debt to Equity is",round(s,2)
    
    
def interest_coverage_ratio():
    """Interest Coverage Ratio"""
    x = float(input("Please Enter Net Income Value: "))
    y = float(input("Please Enter Income Tax Expense Value: "))
    z = float(input("Please Enter Interest Expense Value: "))
    eb = float(x)+float(y)+float(z)
    s = (float(x)+float(y)+float(z))/float(z) 
    print ">> Your Earning Before Interest And Tax (EBIT) is",eb
    print ">> Your Interest-Coverage Ratio is",round(s,2)
    
    
def return_on_sales():
    """Return On Sales"""
    x = float(input("Please Enter Net Income Value: "))
    y = float(input("Please Enter Net Sales Value: "))
    s = (float(x)/float(y))*float(100)
    print ">> Your Return On Sales is",round(s,1),"%"
    
    
    
def return_on_total_assets():
    """Return On Total Assets"""
    x = float(input("Please Enter Net Income Value: "))
    y = float(input("Please Enter Interest Expense Value: "))
    z = float(input("Please Enter Beginning Total Assets Value: "))
    w = float(input("Please Enter Ending Total Assets Value: "))
    d = ((float(x)+float(y)) / ((float(z)+float(w)) / float(2))) * float(100)
    print ">> Your Rate of Return on Total Assets is",round(d,1),"%"
    
    
def asset_turnover():
    """Asset TurnOver"""
    x = float(input("Please Enter Net Sales Value: "))
    y = float(input("Please Enter Beginning Total Assets Value: "))
    z = float(input("Please Enter Ending Total Assets Value: "))
    d = float(x) / ((float(y)+float(z)) / float(2))
    print ">> Your Asset TurnOver Ratio is",round(d,2)
    
    
def ar_turnover():
    """Accounts Receivable TurnOver"""
    x = float(input("Please Enter Net credit sales Value: "))
    y = float(input("Please Enter Beginning Accounts Receivable Value: "))
    z = float(input("Please Enter Ending Accounts Receivable Value: "))
    s = float(x)/((float(y)+float(z))/float(2))
    q = float(365)/float(s)
    print ">> Your Accounts Receivable TurnOver is",round(s,1)
    print ">> Your Days Sales in Receivables is",round(q),"days"
    
    
def return_on_equity():
    """Return On Equity"""
    x = float(input("Please Enter Net Income Value: "))
    s = float(input("Please Enter The Value of Preferred dividend Paid: "))
    y = float(input("Please Enter Beginning common stockholders equity Value: "))
    z = float(input("Please Enter Ending common stockholders equity Value: "))
    d = ((float(x)-float(s)) / ((float(y)+float(z)) / float(2))) * float(100)
    print ">> Your Rate of Return on Common Stockholders Equity is",round(d,1),"%"


def price_earnings():
    """Price Earnings Ratio"""
    x = float(input("Please Enter Market price per share of common stock: "))
    a = float(input("Please Enter Net Income Value: "))
    b = float(input("Please Enter The Value of Preferred dividend Paid: "))
    c = float(input("Please Enter Number of shares of common stock outstanding: "))
    y = (float(a)-float(b))/float(c)
    s = float(x)/float(y)
    print ">> Your Price/Earnings Ratio is",round(s,2)


def dividend_payout():
    """Dividend Payout"""
    x = float(input("Please Enter Annual dividends per share of common stock: "))
    a = float(input("Please Enter Net Income Value: "))
    b = float(input("Please Enter The Value of Preferred dividend Paid: "))
    c = float(input("Please Enter Number of shares of common stock outstanding: "))
    y = (float(a)-float(b))/float(c)
    s = (float(x)/float(y))*float(100)
    print ">> Your Dividend Payout is",s,"%"
    
    
def earnings_per_share():
    """Earnings Per Share"""
    x = float(input("Please Enter Net Income Value: "))
    s = float(input("Please Enter The Value of Preferred dividend Paid: "))
    y = float(input("Please Enter Number of shares of common stock outstanding: "))
    e = (float(x)-float(s)) / float(y)
    print ">> Your Earnings per Share of Common Stock(EPS) is",round(e,2),"\n"
    b = input("      Press 1 To Calculate Dividend Payout on Common Stock\n      Press 2 to Calculate Price/Earnings Ratio\n      Press 3 to Calculate Dividend Yield on Common Stock\n      Or Press 0 to Exit: ")
    if(b == 1):
        u = float(input("Please Enter Annual dividends per share of common stock: "))
        ggg = (float(u) / float(e)) *float(100)
        print ">> Your Dividend Payout on Common Stock is",round(ggg,2),"%"
    elif(b == 2):
        cc = float(input("Please Enter Market price per share of common stock: "))
        eee = float(cc)/float(e)
        print ">> Your Price/Earnings(P/E) Ratio is",round(eee,2)
    elif(b == 3):
        tt = float(input("Please Enter Annual dividends per share of common stock: "))
        cc = float(input("Please Enter Market price per share of common stock: "))
        xxx = (float(tt)/float(cc)) * float(100)
        print ">> Your Dividend Yield on Common Stock is",round(xxx,2),"%"
    elif(b == 0):
        print "Canceled"
            
            
    
    
    
def dividend_yield():
    """Dividend Yield"""
    x = float(input("Please Enter Annual dividends per share of common stock: "))
    y = float(input("Please Enter Market price per share of common stock: "))
    s = (float(x)/float(y))*float(100)
    print ">> Your Dividend Yield is",round(s,1),"%"
    
    
def book_value():
    """Book Value per Share of Common Stock"""
    a = float(input("Please Enter Total Stockholders Equity Value: "))
    b = float(input("Please Enter Preferred Equity Value: "))
    c = float(input("Please Enter Number of Shares of Common Stock Outstanding: "))
    d = (float(a)-float(b))/float(c)
    print ">> Your Book Value Per Share of Common Stock is",round(d,2)
    
    
    
def ratio_analysis():
    """Ratio Analysis"""
    a = float(input("Please Enter Net Income(Loss) Value: "))
    b = float(input("Please Enter Net sales Value: "))
    c = float(input("Please Enter Net Credit Sales Value: "))
    d = float(input("Please Enter The Cost Of Goods Sold(COGS) Value: "))
    e = float(input("Please Enter Interest Expense Value: "))
    f = float(input("Please Enter Income Tax Expense Value: "))
    g = float(input("Please Enter Total Current Assets Value: "))
    h = float(input("Please Enter Beginning Accounts Receivable Value: "))
    i = float(input("Please Enter Ending Accounts Receivable Value: "))
    j = float(input("Please Enter Beginning Inventory Value: "))
    k = float(input("Please Enter Ending Inventory Value: "))
    l = float(input("Please Enter Beginning Total Assets Value: "))
    m = float(input("Please Enter Ending Total Assets Value: "))
    n = float(input("Please Enter Total Current Liabilities Value: "))
    o = float(input("Please Enter Total Liabilities Value: "))
    p = float(input("Please Enter Beginning Total Common Equity Value: "))
    q = float(input("Please Enter Ending Total Common Equity Value: "))
    r = float(input("Please Enter Preferred Dividend Value: "))
    s = float(input("Please Enter Annual Dividends Per Share Of Common Stock Value: "))
    t = float(input("Please Enter Number Of Common Shares Outstanding: "))
    u = float(input("Please Enter Market Price Per Share of Common Stock: "))
    uu = float(g)-float(n) #Working capital
    aa = float(g)/float(n)  #current Ratio
    bb = (float(g)-float(k))/float(n)  #Quick Ratio
    cc = float(d)/((float(j)+float(k))/float(2)) #Inventory turnover
    dd = float(365)/float(cc) #Days in inventory
    ee = float(b)-float(d) #gross margin
    ff = (float(ee)/float(b))*float(100) #Gross profit percent
    gg = float(c)/((float(h)+float(i))/float(2)) #Accounts receivable turnover
    hh = float(365)/float(gg) #days in receivable
    ii = (float(o)/float(m))*float(100) #debt ratio
    jj = float(o)/float(q) #debt to equity
    kk = float(a)+float(f)+float(e) #ebit
    ll = float(kk)/float(e) #interest coverage
    mm = (float(a)/float(b))*float(100) #return on sales
    nn = ((float(a)+float(e))/((float(l)+float(m))/float(2)))*float(100) #return on total assets
    oo = float(b)/((float(l)+float(m))/float(2)) #assets turn over
    pp = ((float(a)-float(r))/((float(p)+float(q))/float(2)))*float(100) #return on common equity
    qq = (float(a)-float(r))/float(t) #EPS
    rr = float(u)/float(qq) #Price/Earnings Ratio
    ss = (float(s)/float(u))*float(100) #Dividend Yield
    tt = (float(s)/float(qq))*float(100) #Dividend Payout
    uull = (float(f)/(float(a)-float(f)))*float(100)
    print ">> Your Working Capital is",uu,"\n"
    print ">> Your Current Ratio is",round(aa,2),"\n"
    print ">> Your Quick (Acid-Test) Ratio is",round(bb,2),"\n"
    print ">> Your Inventory TurnOver is",round(cc,1),"\n"
    print ">> Your Days in Inventory is",round(dd),"days \n"
    print ">> Your Gross Profit(Gross Margin) is",ee,"\n"
    print ">> Your Gross Profit Percentage is",round(ff,1),"%\n"
    print ">> Your Accounts Receivable TurnOver is",round(gg,2),"\n"
    print ">> Your Days Sales in Receivables is",round(hh),"\n"
    print ">> Your Debt Ratio is",round(ii,1),"%\n"
    print ">> Your Debt to Equity Ratio is",round(jj,2),"\n"
    print ">> Your Earning Before Interest and Tax is",kk,"\n"
    print ">> Your Interest Coverage Ratio is",round(ll,2),"\n"
    print ">> Your Rate of Return on Net Sales is",round(mm,1),"%\n"
    print ">> Your Rate of Return on Total Assets is",round(nn,1),"%\n"
    print ">> Your Asset TurnOver Ratio is",round(oo,2),"\n"
    print ">> Your Rate of Return on Common Stockholders Equity is",round(pp,1),"%\n"
    print ">> Your Effective Tax Rate is",round(uull,1),"%\n"
    print ">> Your Earnings per Share of Common Stock(EPS) is",round(qq,2),"\n"
    print ">> Your Price/Earnings Ratio is",round(rr,2),"\n"
    print ">> Your Dividend Yield is",round(ss,1),"%\n"
    print ">> Your Dividend Payout is",tt,"%\n"
    
    
    
def unit_cost(*val):
    """Unit Cost"""
    s = input("To Calculate Cost Per Unit For Services Company Press 1\nTo Calculate Cost Per Unit For Merchandising Company Press 2\nTo Calculate Cost Per Unit For Manufacturing Company Press 3: ")
    if(s == 1):
        a = float(input("Please Enter Total Service Costs (Total Expense) Value: "))
        b = float(input("Please Enter Total Number Of Services Provided: "))
        c = float(a)/float(b)
        print ">> Your Cost Per Service is",c
    elif(s == 2):
        d = float(input("Please Enter Beginning Inventory Value: "))
        e = float(input("Please Enter Net Purchases Value: "))
        f = float(input("Please Enter Freight In Value: "))
        g = float(input("Please Enter Ending Inventory Value: "))
        h = (float(d)+float(e)+float(f))-float(g)
        print ">> Your Cost Of Goods Sold is",h
        for i in val:
            dd = float(h)/float(i)
            print ">> Your Cost Per Unit For",i,"Units is",dd
    elif(s == 3):
        i = float(input("Please Enter Beginning Work in Process Inventory Value: "))
        j = float(input("Please Enter Beginning Direct Materials Inventory Value: "))
        k = float(input("Please Enter Purchases of Direct Materials (including freight in): "))
        l = float(input("Please Enter Ending Direct Materials Inventory Value: "))
        m = float(input("Please Enter Direct Labor Cost Value: "))
        n = float(input("Please Enter Indirect Materials Value: "))
        o = float(input("Please Enter Indirect Labor Value: "))
        p = float(input("Please Enter Depreciation Value (plant and equipment): "))
        q = float(input("Please Enter Plant Utilities and Insurance and Property Taxes Value: "))
        r = float(input("Please Enter Ending Work in Process Inventory Value: "))
        ss = (float(j)+float(k))-float(l)  
        t = float(n)+float(o)+float(p)+float(q)  
        u = (float(i)+float(t)+float(ss)+float(m))-float(r)  
        print ">> Your Total Direct Materials Used is",ss
        print ">> Your Total Manufacturing Overhead Cost is",t
        print ">> Your Cost Of Goods Sold is",u
        for ii in val:
            eee = float(u)/float(ii)
            print ">> Your Cost Per Unit For",ii,"Units is",eee
            
            
            
            
def high_low_method():
    """High Low Method"""
    a = float(input("Please Enter Highest Volume Value: "))
    c = float(input("Please Enter Highest Cost Value: "))
    b = float(input("Please Enter Lowest Volume Value: "))
    d = float(input("Please Enter Lowest Cost Value: "))
    e = float(input("Please Enter Number of Units (To Compute Cost For): "))
    ab = float(a)-float(b)
    cd = float(c)-float(d)
    vr = float(cd)/float(ab)
    fx = float(c)-(float(vr)*float(a))
    mc = float(vr)*float(e)
    mx = float(mc)+float(fx)
    print ">> Your Variable Cost Per Unit is",vr
    print ">> Your Estimated Fixed Cost is",fx
    print ">> Your Estimated Variable Cost is",mc
    print ">> Your Estimated Total Mixed Cost For",e,"Units is",mx
    

def target_profit():
    """Target Profit"""
    a = float(input("Please Enter Sales Price Per Unit: "))
    b = float(input("Please Enter Variable Cost Per Unit: "))
    c = float(input("Please Enter Your Target Profit: "))
    d = float(input("Please Enter Total Fixed Cost: "))
    e = float(a)-float(b)
    f = (float(d)+float(c))/float(e)
    g = float(e)/float(a)
    gg = float(g)*float(100)
    h = (float(d)+float(c))/float(g)
    print ">> Your Contribution Margin is",e
    print ">> Your Contribution Margin Ratio is",gg,"%"
    print ">> Your Target Profit in Units To Earn",c,"$ is",round(f)
    print ">> Your Target Profit in Dollars To Earn",c,"$ is",h




def margin_of_safety():
    """Margin of Safety"""
    a = float(input("Please Enter Sales Price Per Unit: "))
    b = float(input("Please Enter Variable Cost Per Unit: "))
    bb = float(input("Please Enter Total Fixed Cost: "))
    c = float(input("Please Enter Expected Sales: "))
    d = float(a)-float(b)
    e = float(bb)/float(d)
    f = float(c)-float(e)
    g = float(f)*float(a)
    print ">> Your Margin of Safety in Units is",f
    print ">> Your Margin of Safety in Dollars is",g


    
def cost_volume_profit():
    """Cost Volume Profit Analysis"""
    c = float(input("Please Enter Total Fixed Costs Value: "))
    a = float(input("Please Enter Sale Price Per Unit: "))
    b = float(input("Please Enter Variable Cost Per Unit: "))
    ccm = float(a)-float(b)
    cuu = float(c)/float(ccm)
    ccmr = (float(ccm)/float(a))*float(100)
    cda = float(c)/(float(ccmr)/float(100))
    print ">> Your Contribution Margin is",ccm
    print ">> Your Breakeven Sales in Units is",round(cuu)
    print ">> Your Contribution Margin Ratio is",ccmr,"%"
    print ">> Your Breakeven Sales in Dollars is",cda,"\n"
    qq = input("       Press 1 To Compute Target Profit\n       Press 2 To Compute Margin of Safety\n       Press 3 To Perform Sensitivity Analysis\n       Or Press 0 To Exit: ")
    if(qq == 1):
        dds = float(input("Please Enter Your Target Profit: "))
        xxx = (float(c)+float(dds))/float(ccm)
        xxxx = (float(c)+float(dds))/(float(ccmr)/float(100))
        print ">> Your Target Profit in Units To Earn",dds,"$ is",round(xxx)
        print ">> Your Target Profit in Dollars To Earn",dds,"$ is",xxxx
    elif(qq == 0):
        print "Canceled"
    elif(qq == 2):
        xc = float(input("Please Enter Expected Sales in Units: "))
        zzz = float(xc)-float(cuu)
        zzzz = float(zzz)*float(a)
        print ">> Your Margin of Safety in Units is",round(zzz)
        print ">> Your Margin of Safety in Dollars is",zzzz
    elif(qq == 3):
        i = input("Please Enter Total Fixed Costs Value: ")
        o = input("Please Enter Sale Price Per Unit: ")
        p = input("Please Enter Variable Cost Per Unit: ")
        n = 0
        for x,y,z in zip(i,o,p):
            cm = float(y)-float(z)
            uu = float(x)/float(cm)
            cmr = (float(cm)/float(y))*float(100)
            da = float(x)/(float(cmr)/float(100))
            n += 1
            print "Your Results in Case",int(n),"is :"
            print ">> Your Contribution Margin is",cm
            print ">> Your Breakeven Sales in Units is",round(uu)
            print ">> Your Contribution Margin Ratio is",cmr,"%"
            print ">> Your Breakeven Sales in Dollars is",da,"\n"
            if(cm > ccm):
                a = float(cm)-float(ccm)
                print ">> Your Contribution Margin Increased by",a
            elif(ccm > cm):
                a = float(ccm)-float(cm)
                print ">> Your Contribution Margin Decreased by",a
            if(uu > cuu):
                b = float(uu)-float(cuu)
                print ">> Your Breakeven Sales in Units Increased by",round(b)
            elif(cuu > uu):
                b = float(cuu)-float(uu)
                print ">> Your Breakeven Sales in Units Decreased by",round(b)
            if(cmr > ccmr):
                c = float(cmr)-float(ccmr)
                print ">> Your Contribution Margin Ratio Increased by",c,"%"
            elif(ccmr > cmr):
                c = float(ccmr)-float(cmr)
                print ">> Your Contribution Margin Ratio Decreased by",c,"%"
            if(da > cda):
                d = float(da)-float(cda)
                print ">> Your Breakeven Sales in Dollars Increased by",d
            elif(cda > da):
                d = float(cda)-float(da)
                print ">> Your Breakeven Sales in Dollars Decreased by",d,"\n"
            
            
            
def payback_period():
    """Payback Period"""
    a = input("For Payback with Equal Annual Net Cash Inflows Press 1\nFor Payback with Unequal Net Cash Inflows Press 2: ")
    if (a == 1):
        b = float(input("Please Enter Total Amount Invested: "))
        c = float(input("Please Enter Expected Annual Net Cash Inflow: "))
        d = float(input("Please Enter Investment Useful Life (Years): "))
        e = (float(c)*float(d))-float(b)
        f = float(b)/float(c)
        print ">> Your Payback Period is",f,"Years"
        print ">> Total Amount Remaining After Payback Period is",e,"(Residual Value Not Included)"
    elif(a == 2):
        b = float(input("Please Enter Total Amount Invested: "))
        c = list(input("Please Enter Expected Annual Net Cash Inflow: "))
        n = 0
        t = 0
        ss = sum(c)
        am = float(ss)-float(b)
        if(ss < b):
            print ">> Your Loss On Investment is",abs(am)
        elif(ss > b):
            while t <= b:
                e = c[0 + n]
                t += float(e)
                n += 1
        gg = c[n - 1]
        ii = (float(t)-float(b))/float(gg)
        ccc = float(n)-float(ii)
        print ">> Your Payback Period is",ccc,"Years"
        print ">> Total Amount Remaining After Payback Period is",am
        
        
        
def rate_of_return():
    """Rate Of Return"""
    a = input("For Asset with Equal Annual Net Cash Inflows Press 1\nFor Asset with Unequal Net Cash Inflows Press 2: ")
    if(a == 1):
        b = float(input("Please Enter Annual Cash Inflows For The Asset: "))
        c = float(input("Please Enter Asset Useful Life (Years): "))
        d = float(input("Please Enter Total Depreciation During Operating Life Of Asset: "))
        e = float(input("Please Enter Any Asset Salvage Value: "))
        avo = ((float(b)*float(c))-(float(d)-float(e)))/float(c)
        avi = (float(d)+float(e))/float(2)
        ror = (float(avo)/float(avi))*float(100)
        print ">> Your Average Annual Operating Income From an Asset is",avo
        print ">> Your Average Amount Invested in an Asset is",avi
        print ">> Your Rate Of Return (ROR) is",ror,"%"
    elif(a == 2):
        b = list(input("Please Enter Annual Cash Inflows For The Asset: "))
        d = float(input("Please Enter Total Depreciation During Operating Life Of Asset: "))
        e = float(input("Please Enter Any Asset Salvage Value: "))
        f = sum(b)
        c = len(b)
        g = (float(f)-(float(d)-float(e)))/float(c)
        h = (float(d)+float(e))/float(2)
        ror = (float(g)/float(h))*float(100)
        print ">> Your Average Annual Operating Income From an Asset is",g
        print ">> Your Average Amount Invested in an Asset is",h
        print ">> Your Rate Of Return (ROR) is",ror,"%"
        
                                      
def compound_interest():
    """Compound Interest"""
    ffg = input("If Interest Added Monthly Press 1\nIf Interest Added Annually Press 2: ")
    if(ffg == 1):
        a = float(input("Pleae Enter The Principal Value: "))
        b = float(input("Pleae Enter Interest Rate %: "))
        c = float(input("Please Enter The Loan Period (Months): "))
        t = 0
        n = 0
        g = a
        while c != 0:
            ie = (float(a) * (float(b)/float(100))) * (float(1)/float(12))
            a += float(ie)
            t += float(ie)
            n += 1
            c -= 1
            dd = float(g)+float(t)
            print ">> Your Interest Expense For Month No.",n,"is",ie
        print ">> Your Total Interest Expense For",n,"Months is",t
        print ">> Your Total Payment in Maturity Date is",dd
    elif(ffg == 2):
        a = float(input("Pleae Enter The Principal Value: "))
        b = float(input("Pleae Enter Interest Rate %: "))
        c = float(input("Please Enter The Loan Period (Years): "))
        t = 0
        n = 0
        g = a
        while c != 0:
            ie = float(a) * (float(b)/float(100)) 
            a += float(ie)
            t += float(ie)
            n += 1
            c -= 1
            dd = float(g)+float(t)
            print ">> Your Interest Expense For Year No.",n,"is",ie
        print ">> Your Total Interest Expense For",n,"Years is",t
        print ">> Your Total Payment in Maturity Date is",dd
        
        
        
        
def price_variance():
    """Price Variance"""
    a = float(input("Please Enter Your Actual Price: "))
    b = float(input("Please Enter Your Standard Price: "))
    c = float(input("Please Enter Actual Quantity: "))
    d = float(a)-float(b)
    e = float(d)*float(c)
    print ">> Your Change In Price is",d
    print ">> Your Price Variance is",e
    
    
    
def efficiency_variance():
    """Efficiency Variance"""
    a = float(input("Please Enter Your Actual Quantity: "))
    b = float(input("Please Enter Your Standard Quantity: "))
    c = float(input("Please Enter Your Standard Price: "))
    d = float(a)-float(b)
    e = float(d)*float(c)
    print ">> Your Change In Quantity is",d
    print ">> Your Efficiency Variance is",e
    
    
    
def profit_margin():
    """Profit Margin"""
    a = float(input("Please Enter Operating Income Value: "))
    b = float(input("Please Enter Total Sales Value: "))
    c = (float(a)/float(b))*float(100)
    print ">> Your Profit Margin is",c,"%"
    
    
    
def return_on_investment():
    """Return On Investment"""
    a = float(input("Please Enter Operating Income Value: "))
    b = float(input("Please Enter Beginning Total Assets Value: "))
    c = float(input("Please Enter Ending Total Assets Value: "))
    d = (float(a)/((float(b)+float(c))/float(2)))*float(100)
    print ">> Your Return on Investment (ROI) is",d,"% \n"
    e = input("To Calculate Profit Margin And Asset TurnOver Press 1\n To Exit Press 0: ")
    if(e == 1):
        f = float(input("Please Enter Total Sales Value: "))
        i = (float(b)+float(c))/float(2)
        g = (float(a)/float(f))*float(100)
        h = float(f)/float(i)
        print ">> Your Profit Margin is",g,"%"
        print ">> Your Asset TurnOver is",h
        
        
        
def residual_income():
    """Residual Income"""
    a = float(input("Please Enter Operating Income Value: "))
    b = float(input("Please Enter Your Target Rate Of Return %: "))
    c = float(input("Please Enter Beginning Total Assets Value: "))
    d = float(input("Please Enter Ending Total Assets Value: "))
    e = (float(b)/float(100))*((float(c)+float(d))/float(2))
    f = float(a)-float(e)
    print ">> Your Minimum Acceptable Operating Income is",e
    print ">> Your Residual Income (RI) is",f
                                   
                                   
                                   
def effective_tax_rate():
    """Effective Tax Rate"""
    b = float(input("Please Enter Net Income Value: "))
    a = float(input("Please Enter Income Tax Expense: "))
    c = float(b)+float(a)
    d = (float(a)/float(c))*float(100)
    e = float(100)-float(d)
    f = float(c)*(float(e)/float(100))
    print ">> Your Pre Tax Income is",c
    print ">> Your Effective Tax Rate is",round(d,1),"%"
    print ">> Your After-Tax Operating Income is",f
    
    
    
def economic_value_added():
    """Economic Value Added"""
    a = float(input("Please Enter After Tax Operating Income: "))
    b = float(input("Please Enter Current Liabilities Value: "))
    c = float(input("Please Enter Weighted Average Cost Of Capital (minimum rate of return required) %: "))
    d = float(input("Please Enter Beginning Total Assets Value: "))
    e = float(input("Please Enter Ending Total Assets Value: "))
    f = float(a)-((((float(d)+float(e))/float(2))-float(b))*(float(c)/float(100)))
    print ">> Your Economic Value Added (EVA) is",f