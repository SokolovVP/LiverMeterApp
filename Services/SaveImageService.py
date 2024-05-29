import os
import matplotlib.pyplot as plt
import re


def save_image(filedir, filename, image):

    filepath = str(os.path.normpath(os.path.join(filedir, filename)))

    print('FILEPATH: ', filepath + '.png')

    #plt.imsave(filepath, image)

    return filepath
