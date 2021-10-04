"""
This script shows how we trained SynthSeg.
Importantly, it reuses numerous parameters seen in the previous tutorial about image generation
(i.e., 2-generation_explained.py), which we strongly recommend reading before this one.
"""

# project imports
from SynthSeg.training import training


# path training label maps
path_training_label_maps = '../../data/training_label_maps'
path_model_dir = '../../models/SynthSeg_training'
batchsize = 1

# architecture parameters
n_levels = 5           # number of resolution levels
nb_conv_per_level = 2  # number of convolution per level
conv_size = 3          # size of the convolution kernel (e.g. 3x3x3)
unet_feat_count = 24   # number of feature maps after the first convolution
activation = 'elu'     # activation for all convolution layers except the last, which will use sofmax regardless
feat_multiplier = 2    # if feat_multiplier is set to 1, we will keep the number of feature maps constant throughout the
#                        network; 2 will double them(resp. half) after each max-pooling (resp. upsampling);
#                        3 will triple them, etc.

# training parameters
lr = 1e-4               # learning rate
lr_decay = 0            # learning rate decay (knowing that Adam already has its own internal decay)
wl2_epochs = 1          # number of pre-training epochs with wl2 metric w.r.t. the layer before the softmax
dice_epochs = 100       # number of training epochs
steps_per_epoch = 5000  # number of iteration per epoch


# ---------- Generation parameters ----------
# these parameters are from the previous tutorial, and thus we do not explain them again here

# labels and classes lists
# Please note that here we do not provide the number of non-sided labels.
# This is because the training function will do it, based on the FreeSurfer classification of labels.
path_generation_labels = '../../data/labels_classes_priors/generation_labels.npy'
path_segmentation_labels = '../../data/labels_classes_priors/segmentation_labels.npy'

# shape and resolution of the outputs
target_res = None
output_shape = 96
n_channels = 1

# GMM sampling
prior_distributions = 'uniform'
path_generation_classes = '../../data/labels_classes_priors/generation_classes.npy'

# spatial deformation paramaters
flipping = True
scaling_bounds = .15
rotation_bounds = 15
shearing_bounds = .012
translation_bounds = False
nonlin_std = 3.
bias_field_std = .5

# acquisition resolution parameters
randomise_res = True
blur_range = 1.03

# ------------------------------------------------------ Training ------------------------------------------------------

training(path_training_label_maps,
             path_model_dir,
             generation_labels=path_generation_labels,
             segmentation_labels=path_segmentation_labels,
             batchsize=batchsize,
             n_channels=n_channels,
             target_res=target_res,
             output_shape=output_shape,
             prior_distributions=prior_distributions,
             generation_classes=path_generation_classes,
             flipping=flipping,
             scaling_bounds=scaling_bounds,
             rotation_bounds=rotation_bounds,
             shearing_bounds=shearing_bounds,
             translation_bounds=translation_bounds,
             nonlin_std=nonlin_std,
             randomise_res=randomise_res,
             blur_range=blur_range,
             bias_field_std=bias_field_std,
             n_levels=n_levels,
             nb_conv_per_level=nb_conv_per_level,
             conv_size=conv_size,
             unet_feat_count=unet_feat_count,
             feat_multiplier=feat_multiplier,
             activation=activation,
             lr=lr,
             lr_decay=lr_decay,
             wl2_epochs=wl2_epochs,
             dice_epochs=dice_epochs,
             steps_per_epoch=steps_per_epoch)