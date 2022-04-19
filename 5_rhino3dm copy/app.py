from flask import Flask
import ghhops_server as hs

#notice, we import another file as a library
import geometry as geo


app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/moreRandomPoints",
    name = "More Random Points",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Z range of randomness", "Z", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("T sphere radious", "T", "Sphere radios in points", hs.HopsParamAccess.ITEM)
        

    ],
    outputs=[
       hs.HopsBrep("Sphere","SP","List of generated Spheres ", hs.HopsParamAccess.LIST)
    ]
)
def moreRandomPoints(count,rX, rY, rZ, rT):

    randomsph = geo.createRandomPoints(count,rX, rY, rZ, rT)
    return randomsph




if __name__== "__main__":
    app.run(debug=True)