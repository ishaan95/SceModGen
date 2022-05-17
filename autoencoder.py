import rescale
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

focal_tracks = rescale.getAllFocalTracks()
track_tensors = rescale.rescaleTracks(focal_tracks) # 162x50x2 is the real shape

track_tensors_training_data = track_tensors[0:129]
track_tensors_validation_data = track_tensors[130:161]

# Construct the basic autoencoder model
input = layers.Input(shape=(129, 50, 50, 1))














