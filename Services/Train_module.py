from monai.networks.nets import UNet
from monai.networks.layers import Norm
from monai.losses import DiceLoss, DiceCELoss

import torch


from preprocessing import prepare
from utilities import train, calculate_weights


#data_dir = 'D:/GraduateWorkData/nifti_files2'
data_dir = 'D:/GraduateWorkData/nifti_files2/Dataset80-20'
model_dir = 'D:/GraduateWorkData/nifti_files2/results/results' 

#data_dir = 'D:/GraduateWorkData/nifti_files2/AugmentatedDatasetWithTransform'
#model_dir = 'D:/GraduateWorkData/nifti_files2/AugmentatedResults'


#data_in = preprocess_data(data_dir, cache=True)
data_in = prepare(data_dir, cache=True)

device = torch.device("cuda:0")
model = UNet(
    #dimensions=3,
    spatial_dims=3,
    in_channels=1,
    out_channels=2,
    channels=(16, 32, 64, 128, 256), 
    strides=(2, 2, 2, 2),
    num_res_units=2,
    norm=Norm.BATCH,
).to(device)


#loss_function = DiceCELoss(to_onehot_y=True, sigmoid=True, squared_pred=True, ce_weight=calculate_weights(1792651250,2510860).to(device))
#loss_function = DiceCELoss(to_onehot_y=True, sigmoid=True, squared_pred=True, ce_weight=calculate_weights)
loss_function = DiceLoss(to_onehot_y=True, sigmoid=True, squared_pred=True)
optimizer = torch.optim.Adam(model.parameters(), 1e-5, weight_decay=1e-5, amsgrad=True)

if __name__ == '__main__':
    train(model, data_in, loss_function, optimizer, 600, model_dir)