from PIL import Image
import numpy as np

img = Image.open('maze/maze_01.png')

arr = np.array(img)  # every node -> 4 el array
print(arr.shape)
print(arr[0][0])

img = Image.fromarray(arr, 'RGBA')
img.show()