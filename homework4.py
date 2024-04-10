immutable_var = (1, 2, "a","b")
print(immutable_var)
immutable_var[1][1] = 3 #нельзя поменять, потому что элементы кортежа неизменяемые "это закон!"
print(immutable_var)
mutable_list [1, 2, 'a', 'b', 'Modified']
mutable_list [0][0] = 2 #тот же закон!
print(mutable_list)