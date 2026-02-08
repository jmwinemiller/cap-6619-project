# Setup and Imports
from pathlib import Path
import random
import os
import warnings

from genomic_benchmarks.data_check import (
    info,
    is_downloaded,
    list_datasets,
)
from genomic_benchmarks.loc2seq import download_dataset
import jupyter_capture_output
import keras
from keras import backend as K
from keras.layers import (
    Activation,
    BatchNormalization,
    Conv1D,
    Dense,
    Dropout,
    Flatten,
    GlobalAveragePooling1D,
    Input,
    Lambda,
    MaxPooling1D,
    TextVectorization,
)
from keras.losses import (
    BinaryCrossentropy,
    CategoricalCrossentropy,
)
from keras.metrics import (
    BinaryAccuracy,
    CategoricalAccuracy,
)
from keras.models import Sequential
import keras.ops as ops
import matplotlib.pyplot as plt
from mermaid import Mermaid
import numpy as np
import pandas as pd
import tensorflow as tf


SEED = 1234


os.environ["PYTHONHASHSEED"] = str(SEED)
random.seed(SEED)
np.random.seed(SEED)
keras.utils.set_random_seed(SEED)
tf.random.set_seed(SEED)

# Suppress Keras warnings
warnings.filterwarnings("ignore")
