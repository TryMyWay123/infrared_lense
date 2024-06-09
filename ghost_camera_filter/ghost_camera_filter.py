from PIL import Image
import cv2
import numpy as np 
from camera import *
import sys 

def infrared_filter(image):
    # Convert the image to grayscale using PIL
    grayscale_image = image.convert('RGB')
    
    # Invert the grayscale image to simulate the appearance of infrared
    inverted_image = Image.eval(grayscale_image, lambda x: 255 - x)
    
    # Convert back to OpenCV format
    inverted_cv_image = cv2.cvtColor(np.array(inverted_image), cv2.COLOR_RGB2BGR)
    
    # Apply contrast enhancement using OpenCV
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    equalized_image = clahe.apply(inverted_cv_image[:,:,0])
    
    # Add a false color map for visualization
    infrared_colormap = cv2.applyColorMap(equalized_image, cv2.COLORMAP_JET)
    return infrared_colormap

#Add a list of the pictures to iterate through

image_pil = Image.open('img/hollings_3.jpg') 

image_cv = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
infrared_image = infrared_filter(image_pil)

#Display the original and filtered images
cv2.imshow('Original Image', image_cv)
cv2.waitKey(0)  #Wait for a key press before displaying the next image
cv2.imshow('Infrared Filtered Image', infrared_image)
#Save Image 
cv2.waitKey(0)  #Wait for a key press before closing the windows
cv2.destroyAllWindows()











    

