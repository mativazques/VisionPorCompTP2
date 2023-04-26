#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

drawing = 0
coordenadas = []
 
img = cv2.imread('image.jpg')
img2 = cv2.imread('image.jpg')
img3 = cv2.imread('descargar.png')


rowsSrc, colsSrc = img3.shape[:2]
rowsDst, colsDst = img2.shape[:2]

roi = img[0:rowsSrc, 0:colsSrc ]
img4 = np.zeros(img3.shape, dtype='uint8')
img4_inv = cv2.bitwise_not(img4)

input_pts = np.float32([[0,0], [colsSrc-1,0], [0,rowsSrc-1]])

output_pts = []

def draw_rectangle(event, x, y, flags, param):
 global ix, iy, fx, fy, drawing
 
 if event == cv2.EVENT_LBUTTONDOWN:
  coordenadas.append([x,y])
  drawing += 1
  
 if drawing == 3: 
   drawing = 0
   output_pts = np.float32(coordenadas)
   
   M = cv2.getAffineTransform(input_pts , output_pts)
   dst = cv2.warpAffine(img3, M, (colsDst,rowsDst))
   #cv2.imshow('dst',dst)
  

   #cv2.imshow('mask',blackmask)
      
   dstMask = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
   #blurred = cv2.GaussianBlur(gray, (7, 7), 0)
   #cv2.imshow('mask',blurred)
   #ret, mask = cv2.threshold(dstMask, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
   ret, mask = cv2.threshold(dstMask, 190, 255, cv2.THRESH_BINARY)
   #cv2.imshow('mask',mask)
   mask_inv = cv2.bitwise_not(mask)

   #cv2.imshow('mask',mask_inv)
   
   rowsMask,colsMask = mask.shape[:2]
   
   roi = img[0:rowsMask, 0:colsMask ]
   img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
   #cv2.imshow('bg',img1_bg)
   img2_fg = cv2.bitwise_and(dst,dst,mask = mask_inv)
   #cv2.imshow('fg',img2_fg)
   out = cv2.add(img2_fg, img1_bg)
   cv2.imshow('res',out)
   blackmask = cv2.warpAffine(img4_inv, M, (colsDst,rowsDst))
   olis = cv2.cvtColor(blackmask,cv2.COLOR_BGR2GRAY)
   ret2, black = cv2.threshold(olis, 190, 255, cv2.THRESH_BINARY_INV)
   #cv2.imshow('ress',black)
   bg = cv2.bitwise_and(roi,roi,mask = black)
   cv2.imshow('resd',bg)
   result = cv2.add(bg, out)
   cv2.imshow('resultadofinalisimo',result)
 
   
   #print(output_pts)
   
         

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

def save_image():
 global ix, iy, fx, fy
 crop_img = img[iy:fy,ix:fx]
 cv2.imwrite('resultado_tp1.png', crop_img)
 print("Imagen recortada guardada!")
 
 
def reset_image():
 print("Imagen restablecida!")


while(1):
 cv2.imshow('image', img2)
 k = cv2.waitKey(1) & 0xFF
 if k == ord('g'):
  save_image()
  break
     
 elif k == ord('r'):
  img2 = img
  img = cv2.imread('image.jpg')
  reset_image()
  
 elif k == ord('q'):
  break
cv2.destroyAllWindows()
