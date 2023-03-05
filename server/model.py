from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.colors as mcolors
from color import names
import io

def detectColor(img) -> str:
    img = io.BytesIO(img)
    img = Image.open(img)
   
    img_array = np.array(img)
    img_array_2d = img_array.reshape(img_array.shape[1]*img_array.shape[2], img_array.shape[0])

    kmeans = KMeans(n_clusters=1,n_init=1,random_state=0).fit(img_array_2d)
    dominant_color = kmeans.cluster_centers_[0]

    print(dominant_color)
    r, g, b = dominant_color.astype(int)

    hx = mcolors.rgb2hex((r/255,g/255,b/255))[1:]

    return names[name(names,hx)][1]

def name(arr, target):
    """
    Binary search algorithm that returns the index of the target value
    if found in the array, or the index of the closest value if not found.
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if int(arr[mid][0],16) == int(target,16):
            return mid
        elif int(arr[mid][0],16) > int(target,16):
            hi = mid - 1
        else:
            lo = mid + 1
    if hi < 0:
        return 0
    elif lo >= len(arr):
        return len(arr) - 1
    else:
        return lo if abs(int(arr[lo][0],16) - int(target,16)) < abs(int(arr[hi][0],16) - int(target,16)) else hi
