import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if sum(p)==1:
        x=np.array(x)
        p=np.array(p)   
        return np.dot(x,p)
    else:
        raise ValueError("Error")
    pass
