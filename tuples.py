# TUPLES SYNTAX
tuple_example = (1,2,3,4)

# TUPLES CANNOT BE CHANGED UNLIKE LISTS OR DICTIONARIES!

print(tuple_example[0])
try:
    print(tuple_example[5])
except:
    print(f"That is out of range of the tuple!")

tuple_example.pop[3]

# try:
#     tuple_example.pop(0)
# except:
#     print(f"Again, unlike lists, tuples cannot be changed!")