from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo

app = Flask(__name__)
hops = hs.Hops(app)

#creating the workflow
@hops.component(
    "/createStarGraph",
    name = "Create a Star Graph",
    inputs=[
    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)
    ]
)
def createStarGraph():

    G = geo.createGridGraph()
    GW = geo.addRandomWeigths(G)

    nodes = geo.getNodes(G)
    edges = geo.getEdges(G) 

    return nodes, edges





if __name__== "__main__":
    app.run(debug=True)