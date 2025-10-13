# Spatial PKD Manuscript Analysis

This repository contains the notebooks and utility scripts used to generate the
figures for the Spatial PKD manuscript. Assets are grouped by figure.

## Repository Layout
- `figures/fig0x/` &ndash; Jupyter notebooks for each figure (`Fig01.ipynb`,
  `Fig02_a.ipynb`, etc.).
- `scripts/fig0x/` &ndash; Python helpers called from the notebooks
  (segmentation, cyst perimeter extraction, distance-model training utilities).
- `data/` &ndash; *(planned)* location for large external resources
  (SpaceRanger outputs, single-cell atlases, LIANA tensors, etc.). 
- `env/` &ndash; *(planned)* location for environment descriptors (conda YAML,
  requirements files) once the analysis stack is finalised.

## Access to data matrix
Download `spatial_processed.h5ad` from
[Zenodo record 17279214](https://zenodo.org/records/17279214)
