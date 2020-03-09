import matplotlib.pyplot as plt
from bubble_sort import bubble_sort
import random
import cv2
import numpy as np
import os
import shutil

num_element = int(input('Enter no of elements '))

arr = list(range(num_element+1))
f_arr = random.sample(arr, len(arr))

generate = bubble_sort(f_arr)

fig = plt.figure()
os.mkdir('tmp')

i = 0
for frame in generate:
    i += 1
    plt.bar(arr, height=f_arr)
    plt.savefig('tmp/'+ 'frame' +'.png')
    plt.clf()
    cv2.imshow('Chalo', cv2.imread('tmp/frame.png'))
    cv2.waitKey(1)

shutil.rmtree('tmp')
