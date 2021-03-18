Galaxy10 DECals Dataset (Work in progress)
============================================

For original Galaxy10, look here: https://astronn.readthedocs.io/en/latest/galaxy10.html

This page is the improved Galaxy10 using DECals still work in programm

Acknowledgments are at the end of this README

Download Galaxy10
---------------------------------------

Galaxy10.h5: https://astro.utoronto.ca/~hleung/shared/Galaxy10_DECals.h5  (For testing only, not finalize, still many works need to be done)

SHA256: E7ED36C55E099E500AB5D9B50C0635AC761BE3D9F31398187C127559A2A27C46

Size: 2.54 GB

Introduction
---------------

Galaxy10 DECals is a dataset contains 17736 256x256 pixels colored galaxy images (g, r and z band) separated in 10 classes.

Galaxy10 DECals images come from `DESI Legacy Imaging Surveys`_ and labels come from `Galaxy Zoo`_.

::

    Galaxy10 dataset (17736 images)
    ├── Class 0 (1081 images): Disturbed Galaxies
    ├── Class 1 (1853 images): Merging Galaxies
    ├── Class 2 (2645 images): Round Smooth Galaxies
    ├── Class 3 (2027 images): In-between Round Smooth Galaxies
    ├── Class 4 ( 334 images): Cigar Shaped Smooth Galaxies
    ├── Class 5 (2043 images): Barred Spiral Galaxies
    ├── Class 6 (1829 images): Unbarred Tight Spiral Galaxies
    ├── Class 7 (2628 images): Unbarred Loose Spiral Galaxies
    ├── Class 8 (1423 images): Edge-on Galaxies without Bulge
    └── Class 9 (1873 images): Edge-on Galaxies with Bulge

For more information on the original Galaxy Zoo 2 classification tree: `Galaxy Zoo Decision Tree`_

.. _Galaxy Zoo Decision Tree: https://data.galaxyzoo.org/gz_trees/gz_trees.html

.. image:: galaxy10_examples.png

External Catalog Files
--------------------------

Galaxy Zoo Data Release 2 catalog file ``gz2_hart16.csv`` avaliable at https://data.galaxyzoo.org/

Galaxy Zoo DECals catalog files ``gz_decals_volunteers_ab.csv`` and ``gz_decals_volunteers_c.csv`` avaliable at https://zenodo.org/record/4196267#.YE0oZ69KiUm

See acknowledgments for papers described those catalogs

File Descriptions
------------------

-   | `downloader_gzdes_ab_des_dr8.py`_
    | Python script to download all Galaxy Zoo DECals campaign AB images (requires ``gz_decals_volunteers_ab.csv`` and long time to run)
-   | `downloader_gzdes_c_des_dr8.py`_
    | Python script to download all Galaxy Zoo DECals campaign C images (requires ``gz_decals_volunteers_c.csv`` and long time to run)
-   | `downloader_sdssgz2_des_dr8.py`_
    | Python script to download all Galaxy Zoo Data Release 2 images (requires ``gz2_hart16.csv`` and long time to run)
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

System Requirment
-------------------------

If you want to run the notebooks yourself, most of the data reduction processes requiredTensorflow 2.4 or above with NVIDIA GPU to complete in reasonable time. 

Otherwise just `python >3.6`, `astropy`, `h5py`, `matplotlib`


Galaxy10 Dataset Authors
-------------------------

-  | **Henry Leung** - henrysky_
   | Astronomy Student, University of Toronto

-  | **Jo Bovy** - jobovy_
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