from pizza_function import make_pizza as mp
mp(8,'olives','sausage','anchovies')
#when importing modules you can give the function an alias to be called on for your convenience
import pizza_function as pf 
#you can also give a module an alias as well when importing 
pf.make_pizza(10,'extra cheese','pepperoni')

from pizza_function import * 
