# cap-6619-project
Jordan Winemiller - Deep Learning Project
____
<h2>Deep Learning in Genomic Sequence Benchmarking: Implementing CNNs with a 
Focus in Reproducibility<h2>

### Abstract
As deep learning becomes increasingly prevalent in genomics, maintaining
reproducibility in model development and evaluation is essential. In the
biosciences, particularly for large genomic sequence datasets, benchmarking
has become a valuable tool for enabling repeatable sequence classification
experiments. This project uses publicly available genomic sequence benchmark
datasets to implement convolutional neural networks *(CNNs)* for
regulatory element classification and to examine the practical challenges of
reproducing published workflows. We reimplement baseline CNN models using
contemporary deep learning libraries, document the full training and evaluation
pipeline, and compare our results with those reported in prior work. In doing
so, we highlight common issues arising from unmaintained code bases, including
dependency incompatibilities and undocumented preprocessing steps, and assess
their impact on downstream performance and repeatability. The outcome is a
transparent, reproducible set of scripts and guidelines intended to help
students and researchers reliably apply deep learning to benchmark genomic
sequence datasets.


### Project Links
**Files At Root Directory:**
JordanWinemiller-PP.pdf - PowerPoint in Latex with Beamer
JordanWinemiller-Report.pdf - Journal Article in Latex
CAP6619-JordanWinemiller-Presentation.mp4 - Presentation

[*Colab Project Link*](
https://colab.research.google.com/drive/1bx2C30r8Bm4BuFnv6Ugh0vlni72YpwoI)

[*Project Github Link*](
https://colab.research.google.com/drive/1bx2C30r8Bm4BuFnv6Ugh0vlni72YpwoI)

[*Overleaf Report*](
https://www.overleaf.com/read/mkskrfqrrztb#35502b)

### Project Structure
- Presentation: code for LaTex and Powerpoint presentation
  - Assets: diagrams and images to support the presentation
- Report: code and objects for LaTex Report
  - Assets: diagrams and images to support the report
- Resources: original source materials and references
- Src: source code and examples for the project
  - Code Examples: Excerpts from the notebook code
  - Data: information around the data used in the project
  - Diagrams: code for working with mermaid-py
  - Notebooks: all working code for the project
```
Project-Root/
├── presentation
│   └── assets
│       ├── diagrams
│       └── model_runs
├── report
│   └── assets
│       ├── diagrams
│       └── model_runs
├── resources
│   └── bib
└── src
    ├── code_examples
    ├── data
    ├── diagrams
    └── notebooks
```




