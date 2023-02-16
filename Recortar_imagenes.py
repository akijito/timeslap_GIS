#Importar librerias
import os
from osgeo import gdal
#Carpeta donde estan guardadas cada imagen
#Debes tener todas las carpetas dentro de una sola carpeta
path = 'C:/Imagenes'

#Generar una lista con el nombre de las carpetas de cada imagen
pathfolder = os.listdir(path)

#Creamos una lista vacia
path_img = []
for folder in pathfolder:
    img_folder = os.listdir(os.path.join(path, folder))
    img_tif = [f for f in img_folder if f.endswith('.TIF')]
    for img in img_tif:
        img_tif2 = os.path.join(path, folder, img)
        path_img.append(img_tif2)

output_folder ='D:/cut' #Dirección de la carpeta para guardar imagenes recortadas
path_poligon ='D:/area_amz.shp' #Dirección del poligono de recorte
#Combinación de bandas RGB
rgb_L8 = ['B4', 'B3', 'B2']
rgb_L5 = ['B3', 'B2', 'B1']

for i in path_img:
    a = i.split('\\')[2]
    if a[:4] == 'LC08':
        if i[-6:-4] in rgb_L8:
            options = gdal.WarpOptions(cutlineDSName=path_poligon, cropToCutline=True)
            outBand = gdal.Warp(srcDSOrSrcDSTab=i,
                                destNameOrDestDS=output_folder + a[:-4]+'_c1'+a[-4:],
                                options=options)
            outBand = None
    if a[:4] == 'LT05':
        if i[-6:-4] in rgb_L5:
            options = gdal.WarpOptions(cutlineDSName=path_poligon, cropToCutline=True)
            outBand = gdal.Warp(srcDSOrSrcDSTab=i,
                                destNameOrDestDS=output_folder + a[:-4]+'_c1'+a[-4:],
                                options=options)
            outBand = None
