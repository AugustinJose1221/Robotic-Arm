import tinyik as ti
import numpy as np

arm = ti.Actuator(['z',[1.0,0.0,0.0],'z',[1.0,0.0,0.0]])
print(arm.angles,"\n")
print(arm.ee,"\n")
#forward kinematics
arm.angles = [np.pi/6, np.pi/3]
print(arm.ee,"\n")
#reserse kinematics
arm.ee = [2/np.sqrt(2), 2/np.sqrt(2), 0.0]
print(arm.angles,"\n")
print(np.round(np.rad2deg(arm.angles)),"\n")
