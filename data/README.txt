SULI Summer 2021 Project README

Author: Morgan Aire

----------------------------------------------

Hello! This README is designed to summarize the code which was created this summer and provide instructions on the many steps required 
to run the ultimate U-Net code. Please note that many of the files on this folder are unfinished and unnecessary for using the U-Net
model. The numbered list shows the order in which each file should be used. 

----------------------------------------------


1. Napari.ipynb
    This notebook uses Napari to create masks for each image. It includes some preprocessing on the image because Napari has limited image editing software, which made it difficult to see the full image. 
    
    Preprocessing used:
        - Changing any pixel above 10,000 (also works with 1,000) to zero
        - Taking log of each value (FOR CSX DATA: print the min value and add 1+min_val for each point because the log cannot be 
        negative)
        - Change all nans to zero
        - Change pixels above 1,000 to zero (may not be necessary to do this twice)
        - Apply boxcox filter
        
    We also plotted each image using MatPlotLib for comparison. Image will automatically open in Napari.
    
    
    NAPAPRI: 
        Napari will open in a separate window with the image displayed. Here is the process of how I labeled the data to create a mask. 
        1. 
    
    
    NOTE: I created a separate conda environment for Napari in order to use it. All other files used an environment with PyTorch on  
    it. 


2. cropping_data.ipynb
    This notebook crops all input images to a certain size. It crops either using center of mass (if the image is in the middle), 
    cropping on top, or cropping on the side (if image is on the side). We used this notebook to make sure we were focusing on the 
    streaks rather than on feeding the model many blank images without streaks or beam stops. Each crop is commented out and can be
    swapped according to the needs. There are plots to see the images and the masks. 
    
    Note: This notebook opens the original image as well as the masked image. A mask needs to be created before. All output from this
    notebook is saved in the cropped_images and cropped_masks folder. 
    
3. save_raw_data.ipynb
    This notebook takes all of the cropping (or uncropped) data and will save it as a pytorch dictionary of values, where the mask and 
    the input data are combined together in a dictionary. At this point, all data is renamed (data0, data1, etc.)
    
    The file also saves a CSV file of all the names and addresses of each newly created file. This is critical for U-Net to be able to 
    read in the data. 
    
    TODO: possibly add a third key in the dictionary where the original name is tied to each image. 
    TODO: This notebook can easily be removed if a couple other notebooks are modified to include this function in their saving methods. 
    
4. unet/data/save_data.ipynb
    This notebook preprocesses the data and takes n number of random crops of each image. These processed images are then all saved into another folder along with a csv guide of the images. This notebook is very similar to save_raw_data.ipynb
    
    Data from this notebook is saved to data/cropped_data/
    
------------------------------------------------    
    
5. unet/unet_sim_updated.ipynb

    This notebook holds the U-Net model. It reads in the cropped_data folder and uses that to train the model. 
    
    Potential TO-DOs:
    - Current weight function calculates by batch rather than individually
    - Might change weight function to point-wise
    - Mess with preprocessing within this document
    
    
These should be all the files needed to successfully run U-Net from CSX/CHX images. 


To create simulated data, use /speckle_sim/speckle_generation_updated
    
    
    
    
    
    
    
    
SOURCES:

Information on U-Net implemetnation was used from the following blog post:
    https://amaarora.github.io/2020/09/13/unet.html
The U-Net architecture was largely based on the following GitHub repo:
    https://github.com/amaarora/amaarora.github.io/blob/master/nbs/Training.ipynb