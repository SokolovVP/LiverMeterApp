import monai
from monai.transforms import (
    Compose,
    EnsureChannelFirst,
    LoadImage,
    Resize,
    ToTensor,
    Spacing,
    Orientation,
    ScaleIntensityRange,
    CropForeground,
    Activations
)
from monai.data import NibabelReader

reader = NibabelReader()
_img = reader.read()


class UNetLiverSegmenter:


    def __init__():




    