import tinyik as ti
import numpy as np

arm = ti.Actuator(['z',[1.0,0.0,0.0],'z',[1.0,0.0,0.0]])
print(arm.angles,"\n")
print(arm.ee,"\n")
#forward kinematics
arm.angles = [np.pi/6, np.pi/3]
print(arm.ee,"\n")
#reserse kinematics
x=float(input())
y=float(input())
l=np.sqrt((x*x)+(y*y))
x=0
if l<=2:#for points within the hemisphere of radius 2
    x=1
if x==1 :
   arm.ee = [x, y, 0.0]
   #to account for points that require the joint angle to be less than 90 degree
   if arm.angles[0]<=1.5707933 and arm.angles[0]>=-1.5707933:#pi/2=1.5707933
       print(arm.angles,"\n")
       print(np.round(np.rad2deg(arm.angles)),"\n")
   else:
       print("The given coordinates is not accessible")
else:
    print("The given coordinates are out of bound")


