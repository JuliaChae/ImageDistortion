import numpy as np

def img_distort(img, k_vals):
    # load image params 
    y_dim = img.shape[0]
    x_dim = img.shape[1]
    img_distorted = np.zeros(img.shape).astype(np.uint8)
    y_c = y_dim//2 
    x_c = x_dim//2

    # load distortion params 
    k1 = k_vals[0]
    k2 = k_vals[1]
    k3 = k_vals[2]
    k_pos = k_vals[3]

    if k_pos == 1:
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
                img_distorted[y_distorted][x_distorted]=img[y][x]
            except:
                print("out of bounds")
    return img_distorted 
