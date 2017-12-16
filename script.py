import os, torch
import numpy as np
cur_dir = os.listdir()
for file in cur_dir:
    if file.endswith('.npy'):
        a = np.load(file)
        a = torch.from_numpy(a)
        a = a.view(-1, 480, 640).float()/255.
        x = torch.nn.AvgPool2d(kernel_size=5)
        a = x(torch.autograd.Variable(a))
        torch.save(a, file.replace('.npy', '.torch'))
