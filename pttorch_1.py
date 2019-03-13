import torch
import numpy as np

np_data = np.arange(6).reshape(2, 3)
torch_data = torch.from_numpy(np_data)
tensor2numpy = torch_data.numpy()
print('\nnp_data', np_data, '\ntorch_data', torch_data, '\ntensor2bumpy', tensor2numpy)
print(np.sin(np_data))
