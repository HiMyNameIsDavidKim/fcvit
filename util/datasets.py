# References:
# DeiT: https://github.com/facebookresearch/deit
# MAE: https://github.com/facebookresearch/mae
# --------------------------------------------------------


import os
import PIL

from torchvision import datasets, transforms


def build_dataset(is_train, args):
    transform = build_transform(args)

    root = os.path.join(args.data_path, 'train' if is_train else 'val')
    dataset = datasets.ImageFolder(root, transform=transform)

    print(dataset)

    return dataset


def build_transform(args):
    if args.size_puzzle == 225:
        transform = transforms.Compose([
            transforms.Resize(256, interpolation=PIL.Image.BICUBIC, antialias=True),
            transforms.CenterCrop(224),
            transforms.Pad(padding=(0, 0, 1, 1)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        return transform
    if args.size_puzzle == 224:
        transform = transforms.Compose([
            transforms.Resize(256, interpolation=PIL.Image.BICUBIC, antialias=True),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        return transform
