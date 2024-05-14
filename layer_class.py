import torch.nn as nn

class PyTorchNN(nn.Module):

    # constructor
    def __init__(self):
        """
        Assigning Linear Layers to class members variables
        """
        super(PyTorchNN, self).__init__()
        self.layer1 = nn.Linear(in_features=4, out_features=10)
        self.layer2 = nn.Linear(in_features=10, out_features=10)
        self.layer3 = nn.Linear(in_features=10, out_features=10)
        self.layer4 = nn.Linear(in_features=10, out_features=2)

    # predictor
    def forward(self, x):
        """
        Append Layers
        """
        y = nn.Sequential(self.layer1,
                          self.layer2,
                          nn.Sigmoid(),
                          self.layer3,
                          self.ReLU(),
                          self.layer4,
                          nn.Softmax( dim = 1 ))(x)
        return y
