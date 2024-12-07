SALES_TAX_RATE = 7
Sentinel = -1
VariableSimbolica = None
price, actualPrice, salesTax = 0, 0, 0
totalPrice, totalActualPrice, totalSalesTax = 0.0,0.0, 0.0

mensaje="Enter the tax-inclusive price in Euros (or press -1 to exit): "

price = float(input(mensaje))
if(price != Sentinel):
    while(price != Sentinel):
        
        if(price < Sentinel):
            print("Imposible value, type again. ")
            price = float(input(mensaje))
        else :   
            totalPrice += price
            actualPrice = price/((SALES_TAX_RATE/100)+1)     
            salesTax = price-actualPrice
            print("Actual price is: ",'%.2f' % actualPrice,", Sales Tax is: ",'%.2f' % salesTax)
            totalActualPrice += actualPrice; totalSalesTax += salesTax
            price = float(input(mensaje)) 
                
print("Total price is: ",totalPrice)
print("Total actual price es: ",totalActualPrice)
print("Total Sales Tax is: ",totalSalesTax)

