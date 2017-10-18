# -*- coding: utf-8 -*-

""" AlexNet.
Applying 'Alexnet' to Oxford's 17 Category Flower Dataset classification task.
References:
    - Alex Krizhevsky, Ilya Sutskever & Geoffrey E. Hinton. ImageNet
    Classification with Deep Convolutional Neural Networks. NIPS, 2012.
    - 17 Category Flower Dataset. Maria-Elena Nilsback and Andrew Zisserman.
Links:
    - [AlexNet Paper](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
    - [Flower Dataset (17)](http://www.robots.ox.ac.uk/~vgg/data/flowers/17/)
"""

from __future__ import division, print_function, absolute_import

import numpy as np
from numpy import array
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression
from tflearn.data_utils import image_preloader
from tflearn.data_utils import build_hdf5_image_dataset
import h5py

dataset_file = './data/index.txt'
X, Y = image_preloader(dataset_file, image_shape=(227, 227), mode='file', normalize=True)


# build_hdf5_image_dataset(dataset_file, image_shape=(227, 227),
#                          mode='file', output_path='dataset.h5', normalize=True)
# h5f = h5py.File('dataset.h5', 'r')
# X = h5f['X']
# Y = h5f['Y']

print('Start building ...')
# Building 'AlexNet'
network = input_data(shape=[None, 227, 227, 3])
network = conv_2d(network, 96, 11, strides=4, activation='relu')
network = max_pool_2d(network, 3, strides=2)
network = local_response_normalization(network)
network = conv_2d(network, 256, 5, activation='relu')
network = max_pool_2d(network, 3, strides=2)
network = local_response_normalization(network)
network = conv_2d(network, 384, 3, activation='relu')
network = conv_2d(network, 384, 3, activation='relu')
network = conv_2d(network, 256, 3, activation='relu')
network = max_pool_2d(network, 3, strides=2)
network = local_response_normalization(network)
network = fully_connected(network, 4096, activation='tanh')
network = dropout(network, 0.5)
network = fully_connected(network, 4096, activation='tanh')
network = dropout(network, 0.5)
network = fully_connected(network, 17, activation='softmax')
network = regression(network,
                     optimizer='momentum',
                     loss='categorical_crossentropy',
                     learning_rate=0.002)

# Training
model = tflearn.DNN(network,
                    checkpoint_path='model_alexnet',
                    tensorboard_dir='/tmp/tflearn_logs/',
                    best_checkpoint_path='best_model_alexnet',
                    max_checkpoints=1,
                    tensorboard_verbose=3)


print('Start training ...')
model.fit(X, Y,
          n_epoch=2,
          validation_set=0.1,
          shuffle=True,
          show_metric=True,
          batch_size=64,
          snapshot_step=200,
          snapshot_epoch=False,
          run_id='alexnet_oxflowers17')

model.save('my_model.tflearn')