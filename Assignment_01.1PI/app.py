from flask import Flask
import ghhops_server as hs


import geometry as geo
import rhino3dm as rg
import random as r


app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/pointat",
    name = "Point in Curve",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to Eval"),
        hs.HopsNumber("t","t", "Parameter on Curve to Evaluate", default=1.0)      
              
    ],
    outputs=[
       hs.HopsPoint("Point","P","Point on Curve at T")
       
    ]
)

def pointat(curve:rg.Curve, t:float):
    return curve.PointAt(t)
    

@hops.component(
    "/spheresFromPt",
    name = "Spheres from points",
    inputs=[
        hs.HopsPoint("Centers", "C", "Centers", hs.HopsParamAccess.LIST),
        hs.HopsNumber("Radius", "R", "Radius", hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsBrep("Spheres", "S", "Spheres", hs.HopsParamAccess.LIST),
    ],
)
def sphereTest(centers: rg.Point3d, radi):
    spheres = []
    for i in range(len(radi)):
        s = rg.Sphere.ToBrep(rg.Sphere(centers[i], radi[i]))
        spheres.append(s)
    
    return spheres


if __name__== "__main__":
    app.run(debug=True)