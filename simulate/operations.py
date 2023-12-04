BACKEND = 'jax'
DEVICE = 'cpu'

import numpy as np
import scipy as sp
import jax.numpy as jnp
import jax

import torch 
from . import utils

def power(x, p):
    if BACKEND == 'jax':
        return jnp.power(x, p)
    elif BACKEND == 'torch':
        device = torch.device(DEVICE)
        return torch.pow(x, p)
    elif BACKEND == 'numpy':
        return np.power(x, p)


def cdist(x1, x2):
    device = torch.device(DEVICE)
    if BACKEND == 'jax':
        ret = jnp.array(sp.spatial.distance.cdist(x1, x2))
    elif BACKEND == 'numpy':
        ret = np.array(sp.spatial.distance.cdist(x1, x2))
    elif BACKEND == 'torch':
        x1, x2 = map(lambda x: x.to(device), utils.np2tensor(x1, x2))
        ret = torch.cdist(x1, x2)
    return ret