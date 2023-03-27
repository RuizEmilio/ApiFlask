from flask import Flask

app = Flask(__name__)

@app.route('/members' , methods = ['POST'])
def members() :
    return({

        'members' : ['Member1','Member3','Member3']

    })

if __name__ == '__main__' :
    app.run(debug = True)