import cv2
import numpy as np
import matplotlib.pyplot as plt
import os 

from distort import img_distort
from undistort import img_undistort

# load image 
img = cv2.imread('Image2.jpg')
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# distort image 
k_vals = [0.1,0.1,0.1,1] #[k1,k2,k3,pos] where pos =1 if k values are pos and 0 if neg
img_distorted_RGB = img_distort(img_RGB, k_vals)
undistort = img_undistort(img_distorted_RGB, k_vals, 3)

img_distorted = cv2.cvtColor(img_distorted_RGB, cv2.COLOR_RGB2BGR)

# save distorted image
path = os.path.abspath(os.getcwd())
k_text = "k1="+str(k_vals[0])+" k2="+str(k_vals[1])+" k3="+str(k_vals[2])
k_save = "k1="+str(k_vals[0])+"_k2="+str(k_vals[1])+"_k3="+str(k_vals[2])
cv2.putText(img_distorted, k_text, (50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 255, 0), 2)
cv2.imwrite(path+'\\distorted_images\\' +k_save+'.png',img_distorted)

# show distorted and recovered image 
plt.imshow(img_distorted_RGB)
plt.show()
plt.imshow(undistort)
plt.show()




