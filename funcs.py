



# def get_func(a, b):
#     c = a + b
#     d = a - b
#     e = a * b
#     f = a / b
#     print("return value")
#     return c, d, e, f
# a=100
# b=5
# result = get_func(a,b)
# print(result)


# def my_function(a):
#   for x in a:   
#     if x ==5:
#      print()





# def my_function(**boy):
#     print("His date of birth is " + boy["dob"])

#     my_function(fname = "Tobias" , lname = "refnes", dob = "2 jun 2007")


def my_function(a):
    for x in a:
        if x == 5:
            print("Reached to 5")
        else:
            print(x)
        
a = [1,2, "Nothing", 4, 5, "I am Here", 7, False, 9, 10.55]               
my_function(a) 