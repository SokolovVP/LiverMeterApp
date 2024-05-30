import os
import matplotlib.pyplot as plt


def save_image(filedir, filename, image):

    filepath = str(os.path.normpath(os.path.join(filedir, filename)))

    plt.imsave(filepath+'.png', image, cmap='gray')

    return filepath
