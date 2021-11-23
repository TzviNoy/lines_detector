import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from detectors import lines_detector, create_detectors_dict

path = r"images"
images = os.listdir(path)
detectors_dict = create_detectors_dict()

for image in images:  # iterate over all images in path
    for key, value in detectors_dict.items():  # iterate over methods for lines detection

        full_image_path = os.path.join(path, image)  # full path is the images folder path and specific image name/id
        pil_image = Image.open(full_image_path)  # opens image with pil library
        numpy_image = np.array(pil_image)  # converts pil image to numpy array
        highlighted_lines = lines_detector(value, image)  # returns an image with highlighted lines
        path_to_save = os.path.join(some_path, key)
        plt.imsave(path_to_save, highlighted_lines)  # save the highlighted lines image
