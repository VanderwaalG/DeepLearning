import torch.nn as nn
import torch

class moudle3_2(nn.Module):
    def __init__(self):
        super().__init__()
        self.module = nn.Sequential(
            nn.Linear(4,5),
            nn.Linear(5,6),
            nn.Linear(6,4),
            nn.Linear(4,3)
        )

    def forward(self,x):
        output = self.module(x)
        return output

moudle = moudle3_2()

sum = 0

for param in moudle.parameters():
    sum += torch.numel(param)

print(sum)