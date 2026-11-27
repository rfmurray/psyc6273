from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models

# create an object that will put MNIST images into the required format
preprocess = transforms.Compose([
    transforms.Resize(224),    # resize the image to 224 x 224 pixels
    transforms.ToTensor(),     # convert the image to a tensor
    transforms.Lambda(lambda x: x.repeat(3, 1, 1))])  # convert greyscale to colour (RGB channels)

# create a DataSet object that provides the MNIST dataset
data = datasets.MNIST(root='./data', train=True, download=True, transform=preprocess)

# create a DataLoader object that loads the images in random batches
loader = DataLoader(data, batch_size=64, shuffle=True)

# create an untrained AlexNet network and put it into training mode
model = models.alexnet(num_classes=10, weights=None)  # MNIST has 10 categories
model.train()

# use a cross-entropy loss function
criterion = nn.CrossEntropyLoss()

# use the ADAM version of stochastic gradient descent
optimizer = optim.Adam(model.parameters())

# run through the MNIST dataset ten times
for epoch in range(10):

    # get batches of images and labels
    for images, labels in loader:

        # forward pass
        output = model.forward(images)     # get AlexNet's output for this batch
        loss = criterion(output, labels)   # calculate the loss function

        # backward pass
        optimizer.zero_grad()
        loss.backward()

        # adjust the network weights
        optimizer.step()

        # find the proportion of correct responses on this batch
        # (in a real application, we wouldn't do this for every batch)
        model_labels = output.argmax(dim=1)                 # find the category with the largest probability
        pcorrect = (model_labels==labels).float().mean()    # find the proportion of correct responses
        print(pcorrect)
