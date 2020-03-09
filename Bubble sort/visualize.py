import matplotlib.pyplot as plt
from sorting_algos import bubble_sort
import random
import cv2
import numpy as np
import os
import shutil

num_element = int(input('Enter no of elements '))

arr = list(range(1, num_element+1))
f_arr = random.sample(arr, len(arr))

generate = bubble_sort(f_arr)

fig = plt.figure()
os.mkdir('tmp')

i = 0
for j, k, frame in generate:
    i += 1
    barlist = plt.bar(arr, height=f_arr)
    barlist[j].set_color('g')
    barlist[k].set_color('g')
    plt.axis('off')
    plt.savefig('tmp/'+ 'frame' +'.png')
    plt.clf()
    cv2.imshow('Chalo', cv2.imread('tmp/frame.png'))
    cv2.waitKey(1)

shutil.rmtree('tmp')
