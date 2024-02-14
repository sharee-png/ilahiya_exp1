from flask import *

app=Flask(__name__)

@app.route('/login',methods=['GET'])
def reg():
    uname=request.args.get('fname')
    place=request.args.get("plac")
    return 'sucess '+uname


if __name__=="__main__":
    app.run(debug=True)