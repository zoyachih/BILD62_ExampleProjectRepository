import numpy as np

def logistic_map(x,r):
    return r*x*(1-x)

def logistic_map_time(x0,r,T=1000):
    x_t = np.zeros(T)+x0
    for t in range(T-1):
        x_t[t+1] = logistic_map(x_t[t],r)
    return x_t