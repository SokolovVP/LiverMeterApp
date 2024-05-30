from monai.networks.nets import UNet
from monai.networks.layers import Norm
from monai.utils import first
from monai.inferers import sliding_window_inference
import torch
import numpy as np
from Services.preprocessing import preprocess_nifti


def segment_liver(filepath, weights_dir='D:/GraduateWorkData/nifti_files2/22vs8/results/best_metric_model.pth'):
    data_loader = preprocess_nifti(filepath)

    device = torch.device("cuda:0")
    model = UNet(
        spatial_dims=3,
        in_channels=1,
        out_channels=2,
        channels=(16, 32, 64, 128, 256),
        strides=(2, 2, 2, 2),
        num_res_units=2,
        norm=Norm.BATCH,
    ).to(device)

    model.load_state_dict(torch.load(
        weights_dir
    ))

    model.eval()

    sw_batch_size = 4
    roi_size = (128, 128, 64)
    with torch.no_grad():
        max_image = np.array([0])
        max_segmentation = np.array([0])
        max_sum = np.sum(np.nonzero(max_image))

        test_patient = first(data_loader)
        t_volume = test_patient['vol']

        test_outputs = sliding_window_inference(t_volume.to(device), roi_size, sw_batch_size, model)
        sigmoid_activation = torch.nn.Sigmoid()

        test_outputs = sigmoid_activation(test_outputs)
        test_outputs = test_outputs > 0.37

        for i in range(test_patient['vol'].shape[-1]):
            processed_image = test_outputs.detach().cpu()[0, 1, :, :, i]

            if np.sum(np.nonzero(processed_image) > max_sum):
                max_image = processed_image
                max_segmentation = test_patient['vol'][0, 0, :, :, i]

        print(max_image.numpy().shape, type(max_image.numpy()), max_image.shape)
        return max_image, max_segmentation, np.count_nonzero(max_image.numpy())
