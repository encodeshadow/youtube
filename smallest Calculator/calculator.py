#  step 1:
""" 
    1) get input exprssion. input() taking expression as input..
    2) calcualte it. eval(): to get results..
    3) show result. print(): to show result.
"""


# step 2: 

exp = input();
result = eval(exp)
print(result)


# step 3:
print(eval(input("expression: ")))


# step 4: 
try:
    print(eval(input("expression: ")))
except:
    print("invalid input.")


# step 5: 

# define function..
def smallest_calcultor():
    try:
        print(eval(input("expression:(exit to exit) ")))
    except:
        print("invalid input.")
    smallest_calcultor()

# execute function
smallest_calcultor()

