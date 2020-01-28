import numpy as np

#array를 사용할 수 있게 
def step_function(x):
  y = x > 0
  return y.astype(np.int)
