from flask import Flask
import pydot

app = Flask(__name__)

# THE GRAPH FROM STRING
dot_graph = pydot.graph_from_dot_file('grafo.dot')
graph = dot_graph[0]
first_subgraph = str(graph.get_subgraph_list()[0]) # FIRST SUBGRAPH

# GET ROUTE OF MEMBERS
@app.route('/members' , methods = ['GET' , 'POST'])
def members() :
    return({

        'members' : ['Member1','Member2','Member3']

    })

# GET ROUTE OF ANIMALS
@app.route('/animals' , methods = ['GET' , 'POST'])
def animals() :
    return({

        'animals' : ['dog' , 'cat' , 'turtle']

    })

# GET ROUTE OF GRAPH
@app.route('/graphs' , methods = ['GET' , 'POST'])
def graphs() :
    return({

        'graph' : [first_subgraph]

    })

# DEBUG THE APP
if __name__ == '__main__' :
    app.run(debug = True)