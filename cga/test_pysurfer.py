
# import os
# os.environ['QT_API'] = 'pyqt'
# os.environ['ETS_TOOLKIT'] = 'qt'

from surfer import Brain

# Create a brain object
brain = Brain("fsaverage", "lh", "inflated", subjects_dir="C:\\Users\\Cristina\\nilearn_data\\")

# Display the brain
brain.show_view()