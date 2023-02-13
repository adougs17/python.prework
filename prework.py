#Question 1 
def hello_name(user_name):
    print("Hello "+user_name)
user_name = input("Enter Username: ")
hello_name(user_name)
#Question 2
def first_odd():
    for i in range(1,100):
        if i % 2 != 0:
            fist_odd()
#Question 3
list1 = [15, 19, 25, 69, 89, 257]
print("Largest element is: ", max(list1))
#Question 4
def is_leap_year(a_year):
    a_year=input("Enter a year: " )
if a_year % 4  == 0 and a_year % 100 == 0 and a_year % 400 ==0:
    print("True")
else:
    print("False")
#Question 5
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list) +1))
a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list))
a_list = [1,2,4,5]
print(is_consecutive(a_list))




