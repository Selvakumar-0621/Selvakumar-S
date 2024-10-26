
#1 Expected output of given program

[10, 501, 22, 37, 100, 999, 87, 351]

#The result would be the same given list as all the element in the list is greater than 4.





#2 Python program to check every element in the list is integer or string using lambda function

data = [10, 501, 22, 37, 100, 999, 87, 351]

string_or_int = lambda data: isinstance(data, (str, int))               #isinstance used to verify if a given variable belongs to str or int
                                                                        
results = list(map(string_or_int, data))                                # using map() to iterate over the list

print(results)





#3 Python program to create fibonacci series using lambda funtion

fib = lambda x, y: x + y                                                # using Lambda to calculate next Fibonacci number

x, y = 0, 1                                                             # Assigning Initial values

fibonacci_series = []                                                   # Condition to generate Fibonacci Series
while y <= 50:
    fibonacci_series.append(y)
    x, y = y, fib(x, y)

print(fibonacci_series)






#4 Python program using Regular expressions

import re

class RegularExpression:

    def validate_email(self, email):
       
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]"     # Regular Experssion for emailid with a-z, 0-9, _, ., @, extension.

        if re.match(pattern, email):
           return "Valid email_id"
        else:
           return "Invalid email_id"
        


    def validate_bangladesh_mobile_number(self, mobile_number):

        pattern = r"^(?:\+8801|01)[3-9]\d{8}$"                          # Regular Expression for Bangladesh mobile number starts with +880 or 01 followed by 9 digits

        if re.match(pattern, mobile_number):
           return "Valid Bangladesh Mobile Number"
        else:
           return "Invalid Bangladesh Mobile Number"



    def validate_telephone_number_usa(self, telephone_number):

        pattern = r"^\+1\d{10}"                                          # Regular Expression for USA telephone number starts with +1 followed by 10 digits

        if re.match(pattern, telephone_number):
           return "Valid USA Telephone Number"
        else:
           return "Invalid USA Telephone Number"



    def validate_password(self, password):
       
       pattern = r"^[A-Za-z\d@$!%*?&]{16}"                              # Regular Expression for Alpha-Numeric Password with lowercase, uppercase, spcl char & numbers

       if re.match(pattern, password):
        return "Valid Password"
       else:
        return "Invalid Password"



if __name__ == "__main__":
    selva = RegularExpression()

    email = "selva@guvi.in"
    print(selva.validate_email(email))


    mobile_number = "+8801996409999"
    print(selva.validate_bangladesh_mobile_number(mobile_number))


    telephone_number = "+12124567890"
    print(selva.validate_telephone_number_usa(telephone_number))


    password = "aBcD@$!%*?&12345"
    print(selva.validate_password(password))