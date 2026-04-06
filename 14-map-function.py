####################################################
#
#    What is map() in Python ?
#
#    Python syntax
#        map(function, iterable)
#
#        👉  Accept a function name
#        👉  returns a map object
#        👉  applies every item of iterable (list)
#
#   https://chatgpt.com/g/g-p-69c6734c95d081918b05c8e85d2449c5-python/c/69ccd253-dcd8-83a5-9013-4d6617482688
#
####################################################

print("\n -------- Example-1: Basic Understanding ---------\n")
numbers_list = [1,2,3,4,5]
def square(num):
    return num * num

result_obj = map(square, numbers_list)
print( type(result_obj) )
print(result_obj)

for value in result_obj:
    print(value)

    

print("\n -------- Example-2: Basic Understanding ---------\n")
result_list = list(result_obj) # convert object to list
print( type(result_list) )
print(result_list)
