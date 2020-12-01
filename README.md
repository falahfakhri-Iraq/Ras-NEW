
Raster
======

A simple python convereter to convert sentinel2 jp2 bands to tiff.
Use it to create a dataframe table of jp2 bands and sentinel2 images within the folder.
And count the S2 images and jp2 bands within the folder. 


The code is Python 3.

Installation
============

Fast install:

pip install -i https://test.pypi.org/simple/ Ras-NEW==0.0.1


For a manual install get this package:


wget https://github.com/falahfakhri-Iraq/Raster.zip
unzip Raster.zip
rm Raster.zip
cd Raster
´´´

Install the package:

python setup.py install 
 

Example
=======

´´´python

# Import the required library

from sentinel2 import S2_JP2tiff_Converter as S

# Get the number & Dataframe table of Sentinel 2 images within the giving path or directory

Senti_number = S.Counter('D:\TESTS\TEST_NEW')

# Print out the number of Sentinel 2 within the giving path

print(Senti_number.count)

# Print out the Dataframe table of Sentinel2 images 

print(Senti_number.Senti2_Tabel)

# Get the total number of the *.jp2 bands 

jp2_bands = S.BandsJP2('D:\TESTS\TEST_NEW')
 
# Print out the Dataframe table of the *.jp2 bands

print(jp2_bands.JP2_Tabel)

# Convert all the *.jp2 bands within the giving path or directory to *.tiff format 

jp2_bands.S2Converter('D:\TESTS\TEST_NEW', 'D:\TESTS\TEST_NEW\outputFolder')

´´´

   
    
