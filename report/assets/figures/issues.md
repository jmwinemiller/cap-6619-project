The issues that could not be solve have been added to this text
block so the commands do not execute.

**Tensorflow-Addons Issue:**

`!pip install -q tensorflow-addons`

After I was able to get the package install there
was an issue with the *Keras* version and the removal of the
engine object in the new version of *Keras*. Also a this would 
have only worked for the first tested model. So, a new 
$F_1\ Score$ metric was written instead.

**Torchtext Issue:**

There was problem with the compabitility of the torch version with
torchtext. There also was a problem with the python and cuda 
versions with a older version of torch, but a reinstall was 
attempted.

```python
import torch
print(torch.__version__)
```
<small>
Output:
<br>
2.6.0+cu124
</small>

```python
!python --version

!sudo apt-get -qq install python3.11 \
  python3.11-distutils \
  python3-pip

!sudo update-alternatives --install /usr/local/bin/python3 \
  python3 \
  /usr/bin/python3.11 1

!sudo update-alternatives --config python3
!python --version
```

```python
!pip uninstall torch torchtext -y
!pip cache purg
```

```python
# Example for a specific CUDA version (check PyTorch website for the 
exact command)
!pip install torch==2.2.0 torchvision==0.17.0 torchtext==0.18.0 
torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cu12
```
<small>
Output:
<br>
ERROR: Could not find a version that satisfies the requirement
torchtext==0.18.0 (from versions: 0.5.0, 0.6.0, 0.15.0+cpu, 0.15.1+cpu,
0.15.2+cpu, 0.16.0+cpu, 0.16.1+cpu, 0.16.2+cpu, 0.17.0+cpu).
<br>
ERROR: No matching distribution found for torchtext==0.18.0
</small>

**Genomic-benchmarks Issues:**

These imports were could not be used do to *tensorflow-addons* package
or the version update of *keras*.
```python
from genomic_benchmarks.models.tf import (
    get_basic_cnn_model_v0,
    vectorize_layer,
)
```

These imports relied on the version of *torch* and *torchtext* packages
from the above issue.
```python
from genomic_benchmarks.dataset_getters.pytorch_datasets import (
    get_dataset,
)
from genomic_benchmarks.dataset_getters.utils import (
    build_vocab,
    check_seq_lengths,
    check_config,
    coll_factory,
    LetterTokenizer,
    VARIABLE_LENGTH_DATASETS,
)
from genomic_benchmarks.models.torch import CNN
```

**Dataset Issue:**

Testing moving the datasets from a prefetchdataset to a native *numpy*
arrays.
```python
import tensorflow_datasets as tfds
x1 = np.asarray(list(map(lambda x: x[0], tfds.as_numpy(train_ds))))
x1
```
<small>
Output:
<br>
---------------------------------------------------------------------------
<br>
ValueError                                Traceback (most recent call last)
<br>
      1 import tensorflow_datasets as tfds
<br>
----> 2 x1 = np.asarray(list(map(lambda x: x[0], tfds.as_numpy(train_ds))))
<br>
      3 x1
<br>
ValueError: setting an array element with a sequence. The requested array has
an inhomogeneous shape after 1 dimensions. The detected shape was (16,) + 
inhomogeneous part.
</small>

**Keras Issue (Solved):**

The built-in *F1Score* in the metrics package in *keras* would return this
error when the model was training.
<small>
Output:
<br>
/usr/local/lib/python3.11/dist-packages/keras/src/metrics/f_score_metrics.py 
in _build(self, y_true_shape, y_pred_shape)
<br>
    122     def _build(self, y_true_shape, y_pred_shape):
<br>
    123         if len(y_pred_shape) != 2 or len(y_true_shape) != 2:
<br>
--> 124             raise ValueError(
<br>
    125                 "FBetaScore expects 2D inputs with shape "
<br>
    126                 "(batch_size, output_dim). Received input "
<br>
ValueError: FBetaScore expects 2D inputs with shape (batch_size, output_dim).
Received input shapes: y_pred.shape=(None, 1) and y_true.shape=(None,).
</small>

**Fix:** A function was added to gather the *F1 Score* metric.

**Jupyter Capture Issue:**

The package was successful installed and the cell output capture is reporting
a working status, but outputs are not appearing in the directory. 
*FIX: The capture magic methods did work for some image and text outputs.*

**Mermaid-py Issue:**

The package was cutting off text in the layer diagram. *FIX: I used the online
editor at [Mermaid Live Editor](https://mermaid.live/edit)*