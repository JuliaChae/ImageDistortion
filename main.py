import cv2
import numpy as np
import matplotlib.pyplot as plt 

# load image 
img = cv2.imread('Image2.jpg')
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# load image params 
y_dim = RGB_img.shape[0]
x_dim = RGB_img.shape[1]
img_distorted = np.zeros(RGB_img.shape).astype(np.uint8)
y_c = y_dim//2 
x_c = x_dim//2

# load distortion params 
k_pos = 1
k1 = -0.1
k2 = -0.1
k3 = 0

if k_pos == 0:
    r_max = np.sqrt(2)
    x_scale = 1+ k1*(r_max**2) + k2*(r_max**4) + k3*(r_max**6)
    y_scale = x_scale
else:
    r_max = 1
    x_scale = abs(1+ k1*(r_max**2) + k2*(r_max**4) + k3*(r_max**6))
    y_scale = x_scale

# distort image 
for y in range (0, y_dim):
    for x in range (0, x_dim):
        x_norm = (x-x_c)/x_c
        y_norm = (y-y_c)/y_c 
        r = np.sqrt(x_norm**2 + y_norm**2)
        x_dist_norm = x_norm*(1+k1*(r**2) + k2*(r**4) + k3*(r**6))/x_scale
        y_dist_norm = y_norm*(1+k1*(r**2) + k2*(r**4) + k3*(r**6))/y_scale
        x_distorted = int(x_dist_norm*x_c + x_c) 
        y_distorted = int(y_dist_norm*y_c + y_c) 
        try:
            img_distorted[y_distorted][x_distorted]=RGB_img[y][x]
        except:
            print("out of bounds")

k_text = "k1="+str(k1)+" k2="+str(k2)+" k3="+str(k3)
cv2.putText(img_distorted, k_text, (int(y_dim*0.8),int(x_dim*0.8)),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0), 4)
plt.imshow(img_distorted)
plt.show()




