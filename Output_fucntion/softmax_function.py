def softmax(a):
  c = np.max(a)
  exp_a = np.exp(a-c) #prevent error for overflow.
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a

  return y
