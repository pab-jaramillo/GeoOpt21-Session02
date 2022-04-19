#we import all the libraries that our functions need here too
import random as r
from turtle import rt
import rhino3dm as rg

def createRandomPoints(count,rX, rY, rZ, rT):

    randomsph = []    
    for i in range(count):

        #in each itereation generate some random points
        random_x = r.randrange(-rX, rX,2)
        random_y = r.randrange(-rY, rY,2)
        random_z = r.randrange(-rZ, rZ,2)
        random_t = r.randrange(-rT, rT, 2)

        #create a point with rhino3dm
        random_pt = rg.Point3d(random_x, random_y, random_z)
        random_sp = rg.Sphere.ToBrep(random_pt, random_t)          
        
        #add point to the list
        randomsph.append(random_sp)
        

    return randomsph


    