import numpy as np 
from math import cos , sin ,radians,degrees,atan2,sqrt


class Mat_Passage :

    def __init__(self,i,f,theta,L):
        theta=radians(theta)
        self.i=i
        self.f=f
        self.value=np.array(
            [
            [cos(theta) ,-1*sin(theta),0,L],
            [sin(theta),cos(theta),0,0],
            [0,0,1,0],
            [0,0,0,1]
            ] )



def Cord_otherR(point,mat_Pass):
    x=point[0]
    y=point[1]
    z=point[2]
    Matrice_Point = np.array([[x],[y],[z],[1]])
    if type(mat_Pass)==Mat_Passage :
        Matrice_finale = np.dot(mat_Pass.value,Matrice_Point)
    else:
        Matrice_finale=np.dot(mat_Pass,Matrice_Point)
    point_final=Matrice_finale[:3]
    return point_final
