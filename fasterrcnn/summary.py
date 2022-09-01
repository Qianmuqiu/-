import torch
from torchsummary import summary

from nets.frcnn import FasterRCNN

if __name__ == "__main__":
    device  = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    m       = FasterRCNN(20, backbone = 'vgg').to(device)
    summary(m, input_size=(3, 600, 600))
