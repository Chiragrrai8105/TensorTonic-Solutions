import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code her
    x=np.array(x)
    return 1/(1+np.exp(-x))
    pass