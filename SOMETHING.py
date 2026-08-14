name = input("Enter name: ")
print("Hello", name)

Molisch = input("Enter molisch test result: ").strip().lower()
if Molisch == "positive":
    print("Indicates presence of carbohydrates")
elif Molisch == "negative":
    print("Indicates absence of carbohydrates")
    
else:
    print("Molisch test result should be 'positive' or 'negative'")

Iodine = input("Enter Iodine test result: ").strip().lower()
if Iodine == "positive":
    print("Indicates presence of starch")
elif Iodine == "negative":
    print("Indicates absence of starch")
else:
    print("Iodine test result should be 'positive' or 'negative'")

Benedict = input("Enter Benedict's and Fehling's test result: ").strip().lower()
if Benedict == "positive":
    print("Indicates presence of reducing sugars and go for the next test: Barfoed's test")
    Barfoed = input("Enter Barfoed's test result: ").strip().lower()
    if Barfoed == "positive":
        print("Indicates presence of reducing monosaccharides and go for the next test: Bial's test")
        Bial = input("Enter Bial's test result: ").strip().lower()
        if Bial == "positive":
            print("Indicates presence of pentoses and go for the next test: Seliwanoff's test")
            Seliwanoff = input("Enter Seliwanoff's test result: ").strip().lower()
            if Seliwanoff == "positive":
                print("Indicates presence of keto pentoses")
            elif Seliwanoff == "negative":
                print("Indicates presence of aldo pentoses")
            else:
                print("Seliwanoff's test result should be 'positive' or 'negative'")
        elif Bial == "negative":
            print("Indicates absence of pentoses and go for the next test: Seliwanoff's test")
            Seliwanoff = input("Enter Seliwanoff's test result: ").strip().lower()
            if Seliwanoff == "positive":
                print("Indicates presence of ketohexoses")
            elif Seliwanoff == "negative":
                print("Indicates presence of aldohexoses")
            else:
                print("Seliwanoff's test result should be 'positive' or 'negative'")
        else:
            print("Bial's test result should be 'positive' or 'negative'")
    elif Barfoed == "negative":
        print("Indicates absence of reducing monosaccharides")
    else:
        print("Barfoed's test result should be 'positive' or 'negative'")
elif Benedict == "negative":
    print("Indicates absence of reducing sugars and go for the next test: Seliwanoff's test")
    Seliwanoff = input("Enter Seliwanoff's test result: ").strip().lower()
    if Seliwanoff == "positive":
        print("Indicates presence of ketohexoses")
    elif Seliwanoff == "negative":
        print("Indicates presence of aldohexoses")
    else:
        print("Seliwanoff's test result should be 'positive' or 'negative'")
else:
    print("Benedict's and Fehling's test result should be 'positive' or 'negative'")
