from __future__ import division, print_function, absolute_import


# import numpy as np
# from numpy import array
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression
from tflearn.data_utils import image_preloader

dataset = './data'
datafile = './data/index.txt'
X, Y = image_preloader(dataset,
                       image_shape=(227, 227),
                       mode='folder',
                       files_extension=['.png'])


print('Start building ...')
# Building 'AlexNet'
network = input_data(shape=[None, 227, 227, 4])
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
network = fully_connected(network, 2, activation='softmax')
network = regression(network, optimizer='momentum', loss='categorical_crossentropy',
                     learning_rate=0.002)

# Training
model = tflearn.DNN(network,
                    checkpoint_path='model_alexnet',
                    tensorboard_dir='./logs/',
                    best_checkpoint_path='best_model_alexnet',
                    max_checkpoints=1,
                    tensorboard_verbose=0)


print('Start training ...')
model.fit(X, Y,
          n_epoch=2,
          validation_set=0.1,
          shuffle=True,
          show_metric=True,
          batch_size=100,
          snapshot_epoch=True,
          run_id='alexnet_gist')

model.save('my_model.tflearn')
