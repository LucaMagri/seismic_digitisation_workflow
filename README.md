# Seismic image digitisation and navigation conversion workflow

This repository contains a reproducible workflow for converting digitised seismic profile images into SEG-Y files and for preparing seismic navigation files from extracted line coordinates.

The workflow was developed for seismic profiles compiled from image-based sources, where the seismic section is available as a PNG or TIFF image and navigation needs to be extracted or reformatted for use in seismic interpretation software.

## Repository structure

```text
seismic-digitisation-workflow/
├── notebooks/
│   ├── 01_png_image_to_segy.ipynb
│   ├── 02_tiff_image_to_segy.ipynb
│   └── 04_navigation_txt_to_nav.ipynb
├── scripts/
│   └── 03_extract_qgis_layer_coordinates.py
├── environment.yml
├── requirements.txt
├── .gitignore
├── LICENSE
└── CITATION.cff
```

## Workflow

### 1. Convert PNG seismic images to SEG-Y

Notebook: `notebooks/01_png_image_to_segy.ipynb`

This notebook reads a PNG seismic image, converts it to grayscale amplitude values, stores the image columns as seismic traces, and writes the result as a SEG-Y file using ObsPy.

Use this notebook for PNG seismic sections.

### 2. Convert TIFF seismic images to SEG-Y

Notebook: `notebooks/02_tiff_image_to_segy.ipynb`

This notebook performs the same image-to-SEG-Y conversion for TIFF images. It includes handling for large TIFF files and options for splitting large sections into multiple SEG-Y outputs.

Use this notebook for TIFF seismic sections.

### 3. Extract coordinates from QGIS line layers

Script: `scripts/03_extract_qgis_layer_coordinates.py`

This script is intended to be run inside the QGIS Python console. It extracts vertices from a named QGIS line layer and writes them to a comma-separated text file.

### 4. Convert extracted coordinates to navigation files

Notebook: `notebooks/04_navigation_txt_to_nav.ipynb`

This notebook converts comma-separated coordinate text files into `.nav` files. It includes examples for:

- simple two-point navigation lines;
- reversed shotpoint order;
- navigation lines with more than two coordinate points;
- reversed multi-point navigation lines.


## Installation

Create the Conda environment:

```bash
conda env create -f environment.yml
conda activate seismic-digitisation
```

Alternatively, install the Python dependencies with pip:

```bash
pip install -r requirements.txt
```

## Required Python packages

- numpy
- pillow
- matplotlib
- obspy
- jupyterlab

The QGIS coordinate extraction script must be run inside QGIS because it uses the QGIS Python API (`QgsProject`).

## Suggested citation

Magri, L. (2026). Seismic image digitisation and navigation conversion workflow (v0.1.0). Zenodo. https://doi.org/10.5281/zenodo.22866026
