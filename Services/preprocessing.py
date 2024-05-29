import os
from glob import glob

from monai.transforms import (
    Compose,
    EnsureChannelFirstD,
    LoadImaged,
    Resized,
    ToTensord,
    Spacingd,
    Orientationd,
    ScaleIntensityRanged,
    CropForegroundd,
)
from monai.data import DataLoader, Dataset, CacheDataset
from monai.utils import set_determinism


def prepare(in_dir, pixdim=(2, 2, 1.5), a_min=-100, a_max=400, spatial_size=[128, 128, 64], cache=True):
    set_determinism(seed=0)

    path_train_volumes = sorted(glob(os.path.join(in_dir, "TrainImages", "*.nii.gz")))
    path_train_segmentation = sorted(glob(os.path.join(in_dir, "TrainLabels", "*.nii.gz")))

    path_test_volumes = sorted(glob(os.path.join(in_dir, "TestImages", "*.nii.gz")))
    path_test_segmentation = sorted(glob(os.path.join(in_dir, "TestLabels", "*.nii.gz")))

    train_files = [{"vol": image_name, "seg": label_name} for image_name, label_name in
                   zip(path_train_volumes, path_train_segmentation)]
    test_files = [{"vol": image_name, "seg": label_name} for image_name, label_name in
                  zip(path_test_volumes, path_test_segmentation)]

    train_transforms = Compose(
        [
            LoadImaged(keys=["vol", "seg"]),
            EnsureChannelFirstD(keys=["vol", "seg"]),
            Spacingd(keys=["vol", "seg"], pixdim=pixdim, mode=("bilinear", "nearest")),
            Orientationd(keys=["vol", "seg"], axcodes="RAS"),
            ScaleIntensityRanged(keys=["vol"], a_min=a_min, a_max=a_max, b_min=0.0, b_max=1.0, clip=True),
            CropForegroundd(keys=["vol", "seg"], source_key="vol"),
            Resized(keys=["vol", "seg"], spatial_size=spatial_size),
            ToTensord(keys=["vol", "seg"]),

        ]
    )

    test_transforms = Compose(
        [
            LoadImaged(keys=["vol", "seg"]),
            EnsureChannelFirstD(keys=["vol", "seg"]),
            Spacingd(keys=["vol", "seg"], pixdim=pixdim, mode=("bilinear", "nearest")),
            Orientationd(keys=["vol", "seg"], axcodes="RAS"),
            ScaleIntensityRanged(keys=["vol"], a_min=a_min, a_max=a_max, b_min=0.0, b_max=1.0, clip=True),
            CropForegroundd(keys=['vol', 'seg'], source_key='vol'),
            Resized(keys=["vol", "seg"], spatial_size=spatial_size),
            ToTensord(keys=["vol", "seg"]),

        ]
    )

    if cache:
        train_ds = CacheDataset(data=train_files, transform=train_transforms, cache_rate=1.0)
        train_loader = DataLoader(train_ds, batch_size=1)

        test_ds = CacheDataset(data=test_files, transform=test_transforms, cache_rate=1.0)
        test_loader = DataLoader(test_ds, batch_size=1)

        return train_loader, test_loader

    else:
        train_ds = Dataset(data=train_files, transform=train_transforms)
        train_loader = DataLoader(train_ds, batch_size=1)

        test_ds = Dataset(data=test_files, transform=test_transforms)
        test_loader = DataLoader(test_ds, batch_size=1)

        return train_loader, test_loader


def preprocess_nifti(filepath,
                     pixdim=(2, 2, 1.5), a_min=-100, a_max=400, spatial_size=[128, 128, 64], cache=True):

    path_dict = [{'vol': filepath}]

    transforms = Compose(
        [
            LoadImaged(keys=['vol']),
            EnsureChannelFirstD(keys=['vol']),
            Spacingd(keys=['vol'], pixdim=pixdim, mode=('bilinear')),
            Orientationd(keys=['vol'], axcodes='RAS'),
            ScaleIntensityRanged(keys=['vol'], a_min=a_min, a_max=a_max, b_min=0.0, b_max=1.0, clip=True),
            CropForegroundd(keys=['vol'], source_key='vol'),
            Resized(keys=['vol'], spatial_size=spatial_size),
            ToTensord(keys=['vol']),
        ]
    )

    dataset = Dataset(data=path_dict, transform=transforms)
    data_loader = DataLoader(dataset, batch_size=1)

    return data_loader


