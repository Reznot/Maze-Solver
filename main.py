from PIL import Image
import numpy as np
import glob, os
from node import Node


def main(mazes):
    for maze in mazes:
        filename = os.path.basename(maze).split(".")[0]
        img = Image.open(maze)
        arr = np.array(img)  # every node -> 4 el array -> RGB Color
        x, y, z = arr.shape  # array shape & size

        start, end = find_start_end_nodes(arr, x, y)
        print(start, end)
        # print(arr[0][0])
        save_img(arr, filename)


def init_graph(arr, start):

# def color_path(path):
#

'''
Determines start and end nodes of the maze
'''
def find_start_end_nodes(arr, x, y):
    start_node = []
    end_node = []
    for i in range(x):
        if arr[0][i][0] == 255:
            start_node = [0, i]
            break

    for j in reversed(range(x)):
        if arr[y - 1][j][0] == 255:
            end_node = [y - 1, j]
            break
    return start_node, end_node


def save_img(arr, org_name):
    img = Image.fromarray(arr, 'RGBA')
    img.save(f'.\solved\{org_name}_solved.png')


if __name__ == '__main__':
    images = [f for f in glob.glob('.\maze\*.png')]  # Get list of all maze images
    main(images)
