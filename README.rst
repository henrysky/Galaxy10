Galaxy10 DECals Dataset (Work in progress)
============================================

For original Galaxy10, look here: https://astronn.readthedocs.io/en/latest/galaxy10.html

This page is the improved Galaxy10 using DECals still work in programm

Acknowledgments are at the end of this README

Introduction
---------------

Galaxy10 DECals is a dataset contains xxxxx 256x256 pixels colored galaxy images (g, r and z band) separated in 10 classes.

Galaxy10 DECals images come from `DESI Legacy Imaging Surveys`_ and labels come from `Galaxy Zoo`_.

::

    Galaxy10 dataset (xxxxx images)
    ├── Class 0 (xx images): yy
    ├── Class 1 (xx images): yy
    ├── Class 2 (xx images): yy
    ├── Class 3 (xx images): yy
    ├── Class 4 (xx images): yy
    ├── Class 5 (xx images): yy
    ├── Class 6 (xx images): yy
    ├── Class 7 (xx images): yy
    ├── Class 8 (xx images): yy
    └── Class 9 (x images): yy

For more information on the original Galaxy Zoo 2 classification tree: `Galaxy Zoo Decision Tree`_

.. _Galaxy Zoo Decision Tree: https://data.galaxyzoo.org/gz_trees/gz_trees.html

.. image:: readme.png

System Requirment
-------------------------

Most of the data reduction processes required Tensorflow 2.4 or above with NVIDIA GPU for reasonable performance. Otherwise just `python >3.6`, `astropy`, `h5py`, `matplotlib`

External Catalog Files
--------------------------

Galaxy Zoo Data Release 2 catalog file ``gz2_hart16.csv`` avaliable at https://data.galaxyzoo.org/

Galaxy Zoo DECals catalog files ``gz_decals_volunteers_ab.csv`` and ``gz_decals_volunteers_c.csv`` avaliable at https://zenodo.org/record/4196267#.YE0oZ69KiUm

See acknowledgments for papers described those catalogs

File Descriptions
------------------
-   | `downloader_gzdes_ab_des_dr8.py`_
    | Python script to download all Galaxy Zoo DECals campaign AB images (required ``gz_decals_volunteers_ab.csv``)
-   | `downloader_gzdes_c_des_dr8.py`_
    | Python script to download all Galaxy Zoo DECals campaign C images (required ``gz_decals_volunteers_c.csv``)
-   | `downloader_sdssgz2_des_dr8.py`_
    | Python script to download all Galaxy Zoo Data Release 2 images (required ``gz2_hart16.csv``)
-   | `GZ2-SDSS-dataset.ipynb`_
    | Jupyter Notebook to inspect Galaxy Zoo Data Release 2 catalog ``gz2_hart16.csv``
-   | `GZ-DECaLS-dataset.ipynb`_
    | Jupyter Notebook to inspect Galaxy Zoo DECals catalogs ``gz_decals_volunteers_ab.csv`` and ``gz_decals_volunteers_c.csv``
-   | `CCD-Artifacts.ipynb`_
    | Jupyter Notebook to deal with CCD artifacts
-   | `Size-Estimate.ipynb`_
    | Jupyter Notebook to galaxy size
-   | `Compile-Galaxy10-DES.ipynb`_
    | Jupyter Notebook to compile Galaxy10 DECals

.. _downloader_gzdes_ab_des_dr8.py: downloader_gzdes_ab_des_dr8.py
.. _downloader_gzdes_c_des_dr8.py: downloader_gzdes_c_des_dr8.py
.. _downloader_sdssgz2_des_dr8.py: downloader_sdssgz2_des_dr8.py
.. _GZ2-SDSS-dataset.ipynb: GZ2-SDSS-dataset.ipynb
.. _GZ-DECaLS-dataset.ipynb: GZ-DECaLS-dataset.ipynb
.. _CCD-Artifacts.ipynb: CCD-Artifacts.ipynb
.. _Size-Estimate.ipynb: Size-Estimate.ipynb
.. _Compile-Galaxy10-DES.ipynb: Compile-Galaxy10-DES.ipynb

Download Galaxy10 (Work in progress)
---------------------------------------

Galaxy10.h5: xx

SHA256: xx

Size: xx MB (210,234,548 bytes)

Load with astroNN (Work in progress)
---------------------------------------

.. code-block:: python

    from astroNN.datasets import galaxy10


OR Load with Python & h5py (Work in progress)
----------------------------------------------

You should download Galaxy10.h5 first and open python at the same location and run the following to open it:

.. code-block:: python

    import h5py

Split into train and test set (Work in progress)
--------------------------------------------------

.. code-block:: python

    import numpy as np

Lookup Galaxy10 Class (Work in progress)
--------------------------------------------

You can lookup Galaxy10 class to the corresponding name by

.. code-block:: python

    from astroNN.datasets.galaxy10 import galaxy10cls_lookup

Galaxy10 Dataset Authors
-------------------------

-  | **Henry Leung** - Compile the Galaxy10 - henrysky_
   | Astronomy Student, University of Toronto

-  | **Jo Bovy** - Supervisor of Henry Leung - jobovy_
   | Astronomy Professor, University of Toronto

.. _henrysky: https://github.com/henrysky
.. _jobovy: https://github.com/jobovy

Acknowledgments
--------------------------

1. Galaxy10 dataset classification labels come from `Galaxy Zoo`_
2. Galaxy10 dataset images come from `DESI Legacy Imaging Surveys`_

Galaxy Zoo is described in `Lintott et al. 2008, MNRAS, 389, 1179`_, the GalaxyZoo Data Release 2 is described in `Lintott et al. 2011, 410, 166`_, Galaxy Zoo DECals Campaign is described in 
`Walmsley M. et al., 2021, arXiv:2102.08414`_, DESI Legacy Imaging Surveys is described in `Dey A. et al., 2019, AJ, 157, 168`_

The Legacy Surveys consist of three individual and complementary projects: the Dark Energy Camera Legacy Survey (DECaLS; Proposal ID #2014B-0404; PIs: David Schlegel and Arjun Dey), the Beijing-Arizona Sky Survey (BASS; NOAO Prop. ID #2015A-0801; PIs: Zhou Xu and Xiaohui Fan), and the Mayall z-band Legacy Survey (MzLS; Prop. ID #2016A-0453; PI: Arjun Dey). DECaLS, BASS and MzLS together include data obtained, respectively, at the Blanco telescope, Cerro Tololo Inter-American Observatory, NSF’s NOIRLab; the Bok telescope, Steward Observatory, University of Arizona; and the Mayall telescope, Kitt Peak National Observatory, NOIRLab. The Legacy Surveys project is honored to be permitted to conduct astronomical research on Iolkam Du’ag (Kitt Peak), a mountain with particular significance to the Tohono O’odham Nation.

.. _DESI Legacy Imaging Surveys: https://www.legacysurvey.org/
.. _Galaxy Zoo: https://www.galaxyzoo.org/
.. _Lintott et al. 2008, MNRAS, 389, 1179: https://ui.adsabs.harvard.edu/abs/2008MNRAS.389.1179L/abstract
.. _Lintott et al. 2011, 410, 166: https://ui.adsabs.harvard.edu/abs/2011MNRAS.410..166L/abstract
.. _Walmsley M. et al., 2021, arXiv:2102.08414: https://ui.adsabs.harvard.edu/abs/2021arXiv210208414W/abstract
.. _Dey A. et al., 2019, AJ, 157, 168: https://ui.adsabs.harvard.edu/abs/2019AJ....157..168D/abstract