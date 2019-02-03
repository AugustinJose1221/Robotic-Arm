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
if l<=2 :
   arm.ee = [x, y, 0.0]
   print(arm.angles,"\n")
   print(np.round(np.rad2deg(arm.angles)),"\n")
else:
    print("The given coordinates are out of bound")
    

