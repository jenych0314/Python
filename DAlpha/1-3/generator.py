import pickle

import torch
import torch.nn as nn
from torch.utils.data.dataloader import DataLoader
from torchvision import transforms
from torchvision.datasets import MNIST
from tqdm import tqdm


class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv_features = nn.Sequential(
            nn.Conv2d(1, 4, 5, 1),
            nn.ReLU(),
            nn.Conv2d(4, 12, 5, 1),
            nn.ReLU(),
            nn.Conv2d(12, 36, 5, 1),
            nn.ReLU(),
            nn.Conv2d(36, 128, 5, 1),
            nn.ReLU()
        )
        self.linear_features = nn.Sequential(
            nn.Linear(18432, 1024),
            nn.ReLU(),
            nn.Linear(1024, 128)
        )
        self.classifier = nn.Sequential(
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.conv_features(x)
        x = torch.flatten(x, 1)
        x = self.linear_features(x)
        out = self.classifier(x)
        return out, x


def main():
    device = f'cuda:{0}' if torch.cuda.is_available() else 'cpu'
    with open('./la_mnist.pt', 'rb') as f:
        model = torch.load(f)
    test_dataset = MNIST(root='./data', train=False, transform=transforms.ToTensor(), download=True)
    test_dataloader = DataLoader(test_dataset, batch_size=1, shuffle=False)
    model.eval()
    with torch.no_grad():
        score = 0
        total = 0
        with open(rf"E:\Source\dalpha\cnn_latent\label.csv", 'w') as f:
            f.write("file,label\n")
            for image, label in tqdm(test_dataloader):
                image = image.to(device)
                label = label.to(device)
                model_out, latent = model(image)
                with open(rf"E:\Source\dalpha\cnn_latent\{total}.pkl", "wb") as f2:
                    pickle.dump(latent[0].tolist(), f2)
                f.write(f"{total},{label.item()}\n")
                prediction = torch.argmax(model_out, dim=1)
                for idx in range(len(label)):
                    if label[idx] == prediction[idx]:
                        score += 1
                    total += 1
    print(f"total accuracy: {score / total * 100:.5f}%")


if __name__ == '__main__':
    main()
