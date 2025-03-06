
**Create your conda environment** 
1. Install miniconda
2. Check that you have conda installed. In the terminal (it can be pycharm terminal): `conda --version`
3. Create a conda environment named pysurfer_env with python 3.9 and pyqt=5. In the terminal: `conda create -n pysurfer_env python=3.9 pyqt=5` By default this environment is saved in C:\Users\[YourUsername]\Miniconda3\envs\pysurfer_env
4. Change current pycharm interpreter (.venv) to pysurfer_env. Click in the lower right corner of pycharm (.venv). Add new interpreter -> Add local interpreter. Environment: select existing. Type: conda, Path to conda: C:\Users\Cristina\Miniconda3\condabin\conda.bat. Environment: pysurfer_env
5. Deactivate previous environment if needed. In the terminal: `deactivate`
6. Check that your conda environment is active. In the terminal: `conda activate pysurfer_env`. You should see (pysurfer_env) PS C:\Users\Cristina\repos\hansen_receptors>
7. Install dependencies

**Install dependencies**
1. Install **mayavi**. `pip install git+https://github.com/enthought/mayavi.git`
2. Install **pysurfer**. `pip install git+https://github.com/nipy/PySurfer.git`
3. Check that mayavi is working. Run in the python console:
`from mayavi import mlab
mlab.test_contour3d()
mlab.show()` It should appear a 3d drawing
4. Check that pysurfer is working. Run in the python console: (This does not work because I don't have freesurfer)
`from surfer import Brain
brain = Brain("fsaverage", "lh", "inflated")
brain.show_view()`
5. Install **neuromaps** from github. Clone the repository. Cd into the repo being in the pysurfer_env and `pip install .`
6. Install **netneurotools** from github (branch 0.2.X). `pip install git+https://github.com/netneurolab/netneurotools.git@0.2.X`
7. Install seaborn and tqdm. `pip install seaborn tqdm`

# Info
https://netneurolab.github.io/netneurotools/installation.html