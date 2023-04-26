#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

drawing = 0
coordenadas = []
 
img = cv2.imread('images\DestinoDST.jpg')
img2 = cv2.imread('images\DestinoDST.jpg')
img3 = cv2.imread('images\FuenteSRC.png')

rowsSrc, colsSrc = img3.shape[:2]
rowsDst, colsDst = img2.shape[:2]

img4 = np.zeros(img3.shape, dtype='uint8')
img4_inv = cv2.bitwise_not(img4)

input_pts = np.float32([[0,0], [colsSrc-1,0], [colsSrc-1,rowsSrc-1]])
output_pts = []

def draw_rectangle(event, x, y, flags, param):
 global drawing
 
 if event == cv2.EVENT_LBUTTONDOWN:
  global img2, img3, img4_inv
  
  
  coordenadas.append([x,y])
  drawing += 1
  cv2.circle(img2, (x, y), 4 ,(0, 255, 0), -1)
  
 if drawing == 3: 
   
   output_pts = np.float32(coordenadas)
   
   M = cv2.getAffineTransform(input_pts , output_pts)
   dst = cv2.warpAffine(img3, M, (colsDst,rowsDst))
   
   blackmask = cv2.warpAffine(img4_inv, M, (colsDst,rowsDst))
   bgmask = cv2.cvtColor(blackmask,cv2.COLOR_BGR2GRAY)
   ret2, black = cv2.threshold(bgmask, 190, 255, cv2.THRESH_BINARY_INV)
   
   img2 = img
   bg = cv2.bitwise_and(img2,img2,mask = black)
   
   img2 = cv2.add(bg, dst)
   cv2.imwrite('images/back.jpg', bg)
   cv2.imwrite('images/front.jpg', dst)
   cv2.imwrite('images/resultado_tp2.jpg', img2)
   
   #print(output_pts)
   drawing = 0
   coordenadas.clear()
   
         

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

"""
def save_image():
 global ix, iy, fx, fy
 crop_img = img[iy:fy,ix:fx]
 cv2.imwrite('resultado_tp2.png', crop_img)
 print("Imagen recortada guardada!")
"""

while(1):
 cv2.imshow('image', img2)
 k = cv2.waitKey(1) & 0xFF
 
 if k == ord('q'):
  break
cv2.destroyAllWindows()
