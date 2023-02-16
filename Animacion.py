import os
import numpy as np
import matlotlib.pyplot as plt
from osgeo import gdal
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

folder = '../LinkedIn/Imagenes/'
path = os.listdir(folder)
path_tif = [f for f in path if f.endswith('.tif')]
images_file = []
for file in path_tif:
    images1 = os.path.join(folder, file)
    images_file.append(images1)

images2 = []
for i in range(len(images_file)):
    ds = gdal.Open(images_file[i])
    band1 = ds.GetRasterBand(1)
    band2 = ds.GetRasterBand(2)
    band3 = ds.GetRasterBand(3)
    data1 = band1.ReadAsArray()
    data2 = band2.ReadAsArray()
    data3 = band3.ReadAsArray()
    image = np.dstack((data1, data2, data3))
    images2.append(image)

fig, ax = plt.subplots(1, figsize=[15,10])
def update(i):
    ax.imshow(images2[i])
    ax.axis('off')
    ax.set_title(name[i])
ani = FuncAnimation(fig, update, frames= 12, repeat = True, interval=300)

#Esta parte del código es necesaria si estas trabajando en Jupyter
HTML(ani.to_jshtml())
