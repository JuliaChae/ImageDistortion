import cv2
import numpy as np
import matplotlib.pyplot as plt
import os 

from lib.distort import img_distort
from lib.undistort import img_undistort

# load image 
img = cv2.imread('Images/Original/Image.jpg')
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# distort image 
k_vals = [-0.05,-0.05,-0.05,0] #[k1,k2,k3,pos] where pos = 1 if k values are pos and 0 if neg
k_num = 3 # number of k values to use for recovery of distorted image
img_distorted_RGB = img_distort(img_RGB, k_vals)
img_undistorted_RGB = img_undistort(img_distorted_RGB, k_vals, k_num)

img_distorted = cv2.cvtColor(img_distorted_RGB, cv2.COLOR_RGB2BGR)
img_undistorted = cv2.cvtColor(img_undistorted_RGB, cv2.COLOR_RGB2BGR)

# save distorted image
path = os.path.abspath(os.getcwd())
k_text = "k1="+str(k_vals[0])+" k2="+str(k_vals[1])+" k3="+str(k_vals[2])
k_save = "k1="+str(k_vals[0])+"_k2="+str(k_vals[1])+"_k3="+str(k_vals[2])
cv2.putText(img_distorted, k_text, (50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 255, 0), 2)
cv2.imwrite(path+'\\Images\\Distorted\\' +k_save+'.png',img_distorted)

# save undistorted image
k_text = k_text + " " + str(k_num) + " ks"
k_save = k_save + "_" + str(k_num) + "ks"
path = os.path.abspath(os.getcwd())
cv2.putText(img_undistorted, 'Undistorted '+ k_text, (50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 255, 0), 2)
cv2.imwrite(path+'\\Images\\UnDistorted\\' +k_save+'.png',img_undistorted)

# show distorted and recovered image 
plt.imshow(img_distorted_RGB)
plt.show()
plt.imshow(img_undistorted_RGB)
plt.show()




