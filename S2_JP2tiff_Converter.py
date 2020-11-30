# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:49:45 2020

@author: FALAH FAKHRI

# Contact: falah.fakhri@outlook.com / falah.atta@gmail.com 
"""


import os
from glob import iglob
from os.path import join
import pandas as pd
from osgeo import gdal


    
class Counter:
    """Counts S2.SAFE format in in DataFrame table"""
    
    def __init__(self, directory_path=None):
        
        if directory_path is None:
            
            directory_path = ''
        else:
            self.directory_path = os.chdir(directory_path)
            
        
        print('Start Counter.__init__()')
         
        Sentinel = []
        
        for root, dirs, files in os.walk(".", topdown=False):
            for name in dirs:
                os.getcwd()
                if name.endswith('.SAFE'):
                    
                    Sentinel.append(os.path.join(directory_path, name))
                    
        self.count = (f"Sentinel-2_DATA_SAFE_Format number : {len(Sentinel)}")
        imgs_tabel = pd.DataFrame(Sentinel)
        self.Senti2_Tabel = imgs_tabel.melt(value_name="Sentinel-2_id_(*.SAFE)", var_name='sequence')
         
        print('End Counter.__init__()')
        
        
class BandsJP2(Counter):
    """Count and presents the *.jp2 bands of Sentinel2 in DataFrame table"""
    
    def __init__(self, directory_path):
        
        super().__init__(directory_path)
                
        print('Start BandsJP2.__init__()')
                
        inputFolder = os.path.join(directory_path)
            
        product_path  = 'S2*/GRANULE/L*/IMG_DATA/*.*'
        
        directory_path = sorted(list(iglob(join(inputFolder, '**', product_path), recursive=True)))
        
        self.bands = [file for file in directory_path if file.endswith('.jp2')]   
        
        bands_tabel = pd.DataFrame([self.bands])
       
        self.JP2_Tabel = bands_tabel.melt(value_name="Sentinel-2_bands_id_(*.jp2)", var_name='sequence')
        
        print('End BandsJP2.__init__()')   
        
   
    
    def S2Converter(self, input_directory, output_directory):
        """"Return raster *.tiff bands
        parameters
        ----------
        input_directory: str
                path directory to the Sentinel2 images
        
        output_directory: str
                path directory to save the output convertered bands        
        """
        
        for index, files in enumerate(self.bands):
            tiff_bands_path = os.path.join(output_directory, 
                                           os.path.basename(files)[:-4] + ".tif")
            print("tiff_bands_path=", tiff_bands_path)
           
            srcDS = gdal.Open(files)
           
            gdal.Translate(tiff_bands_path, srcDS, format="GTiff", outputType=gdal.GDT_Float64)
         
def main():
    
    pass
 
if __name__ == '__main__':
    
    main()   
