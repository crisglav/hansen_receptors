
**Create your conda environment** 
1. Install miniconda
2. Check that you have conda installed. In the terminal (it can be pycharm terminal): `conda --version`
3. Create a conda environment named pysurfer_env with python 3.9 and pyqt=5. In the terminal: `conda create -n pysurfer_env python=3.9 pyqt=5` By default this environment is saved in C:\Users\[YourUsername]\Miniconda3\envs\pysurfer_env
4. Change current pycharm interpreter (.venv) to pysurfer_env. Click in the lower right corner of pycharm (.venv). Add new interpreter -> Add local interpreter. Environment: select existing. Type: conda, Path to conda: C:\Users\Cristina\Miniconda3\condabin\conda.bat. Environment: pysurfer_env
5. Deactivate previous environment if needed. In the terminal: `deactivate`
6. Check that your conda environment is active. In the terminal: `conda activate pysurfer_env`. You should see (pysurfer_env) PS C:\Users\Cristina\repos\hansen_receptors>
7. Install dependencies

**Install dependencies**
1. Install **Pysurfer** to visualize the inflated brains. In the terminal: `conda install -c conda-forge pysurfer` Note: You can't just install it with pip in windows because it has complex dependencies with other 3d visualization packages (vkt and pyq5t).
2. Downgrade the packages pyface and traitsui. `conda install -c conda-forge traitsui=7.4.2 pyface=7.4.2`
3. Check that **mayavi** is working. Run in the python console:
`from mayavi import mlab
mlab.test_contour3d()
mlab.show()` I should appear a 3d drawing
4. Check that pysurfer is working. Run in the python console:
`from surfer import Brain
brain = Brain("fsaverage", "lh", "inflated")
brain.show_view()`
5. Install neuromaps from github. Clone the repository. Cd into the repo being in the pysurfer_env and `pip install .`
6. Install netneurotools from github. Clone the repository. Cd into the repo being in the pysurfer_env and `pip install .`
