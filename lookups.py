import numpy as np
from numpy import sin
import timeit
from functools import partial

x = np.ones(1000)

def local_fn(x):
    for i in range(1000): x = sin(x)
        
def global_fn(x):
    for i in range(1000): x = np.sin(x)
    
l_time = timeit.timeit(partial(local_fn, x), number=100)

g_time = timeit.timeit(partial(global_fn, x), number=100)

print(f"Time taken by function in local namespace: {l_time}")
print(f"Time taken by function in global namespace: {g_time}")