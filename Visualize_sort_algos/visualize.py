import matplotlib.pyplot as plt
from sorting_algos import selection_sort
from sorting_algos import bubble_sort
import random
import cv2
import numpy as np
import os
import shutil

num_element = int(input('Enter no of elements '))

arr = list(range(1, num_element+1))
f_arr = random.sample(arr, len(arr))
choice = 2
if choice == 1:
    generate = bubble_sort(f_arr)
elif choice == 2:
    generate = selection_sort(f_arr)

fig = plt.figure()
os.mkdir('tmp')

i = 0
for swap, j, k, frame in generate:
    i += 1
    barlist = plt.bar(arr, height=frame)
    barlist[j].set_color('g')
    barlist[k].set_color('g')
    if swap:
        barlist[j].set_color('y')
        barlist[k].set_color('y')
    #else:
        #barlist[j].set_color('g')
        #barlist[k].set_color('g')
    plt.axis('off')
    plt.savefig('tmp/'+ 'frame' +'.png')
    plt.clf()
    cv2.imshow('Chalo', cv2.imread('tmp/frame.png'))
    cv2.waitKey(1)

shutil.rmtree('tmp')
