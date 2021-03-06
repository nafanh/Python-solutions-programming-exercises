# Monthly_Sales_Tax5_9

# A retail company must file a monthly sales tax report
# listing the total sales for the month, and the amount of state
# and county sales tax collected. The state sales tax rate is 5 percent
# and the county sales tax rate is 2.5 percent.
# Write a program that asks the user to enter the total sales for the month.
# From this figure, the application should calculate and display the following:
# The amount of county sales tax
# The amount of state sales tax
# The total sales tax (county plus state) 


rate_state_tax=0.05
rate_county_tax=0.025

def main():
    total_sales=float(input('Enter the total sales for the month: $ '))
    county_tax=get_county_tax(total_sales)
    sales_tax=get_sales_tax(total_sales)
    total_tax=get_total_tax(county_tax,sales_tax)
    
    print('The amount of county sales tax: $',format(county_tax,'.2f'),sep='')
    print('The amount of state sales tax: $',format(sales_tax,'.2f'),sep='' )
    print('The total sales tax (county plus state: $',format(total_tax,'.2f'),sep='')

def get_county_tax(sales):
    return sales*rate_county_tax
def get_sales_tax(sales):
    return sales*rate_state_tax
def get_total_tax(county,sales):
    return county+sales 

main()
