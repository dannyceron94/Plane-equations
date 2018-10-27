#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:01:03 2018

@author: mayank
"""

x1,y1,z1=eval(input('enter 1st point '))
p1=[x1,y1,z1]

x2,y2,z2=eval(input('enter 2nd point '))
p2=[x2,y2,z2]

x3,y3,z3=eval(input('enter 3rd point '))
p3=[x3,y3,z3]

v1= list(((float(p1[0]-p2[0])),(float(p1[1]-p2[1])) ,(float(p1[2]-p2[2]))))
v2= list(((float(p1[0]-p3[0])),(float(p1[1]-p3[1])) ,(float(p1[2]-p3[2]))))

print (v1,v2)
import numpy as np
x= np.cross(v1,v2)
pln= ('('+str(x[0])+'X'+')'+' '+'+'+' '+'('+str(x[1])+'Y'+')'+' '+'+'+' '+'('+str(x[2])+'Z'+')'+' '+'='+' '+str(x[0]*x1+x[1]*y1+x[2]*z1))
print (pln)