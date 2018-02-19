
# coding: utf-8

# In[1]:


months = int(input("Enter mortgage term (in months): "))
rate = float(input("Enter interest rate: "))
loan = float(input("Enter loan value: "))

monthly_rate = rate / 100 / 12
payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan


def mortgage(months,rate,loan):
    return payment

def main():
    print("Wlecome to Mortgage Calculator")
    print(mortgage(months,rate,loan))
    return;
main()

