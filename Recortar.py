{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ddf3ea5b-758f-4b86-998c-e8aeeb50de48",
   "metadata": {},
   "outputs": [],
   "source": [
    "from osgeo import gdal\n",
    "output ='D:/Proyecto_LinkedIn/Imagenes de satelite/recortadas/'\n",
    "path_cut ='D:/Proyecto_LinkedIn/Imagenes de satelite/Vector/area_amz.shp'\n",
    "def img_cutting_RGB(path_img, output_location, path_cut):\n",
    "    rgb_L8 = ['B4', 'B3', 'B2']\n",
    "    rgb_L5 = ['B3', 'B2', 'B1']\n",
    "    for i in range(len(path_img)):\n",
    "        a = path_img[i].split('/')[-1]\n",
    "        if a[:4] == 'LC08':\n",
    "            if a[-6:-4] in rgb_L8:\n",
    "                name = '/{}_{}_{}_{}_{}.TIF'.format(a[17:21],a[21:23],a[23:25],a[-6:-4],a[:4])\n",
    "                options = gdal.WarpOptions(cutlineDSName = path_cut, cropToCutline = True)\n",
    "                outBand = gdal.Warp(srcDSOrSrcDSTab = path_img[i], \n",
    "                                    destNameOrDestDS = output_location + name,\n",
    "                                    options = options)\n",
    "                outBand = None\n",
    "\n",
    "        if a[:4] == 'LT05':\n",
    "            if a[-6:-4] in rgb_L5:\n",
    "                name = '/{}_{}_{}_{}_{}.TIF'.format(a[17:21],a[21:23],a[23:25],a[-6:-4],a[:4])\n",
    "                options = gdal.WarpOptions(cutlineDSName = path_cut, cropToCutline = True)\n",
    "                outBand = gdal.Warp(srcDSOrSrcDSTab = path_img[i], \n",
    "                                    destNameOrDestDS = output_location + name,\n",
    "                                    options = options)\n",
    "                outBand = None"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
