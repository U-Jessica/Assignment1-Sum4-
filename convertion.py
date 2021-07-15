import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    a=jsonObj['a']
    n=len(a)
    s=0
    for i in range(-(n),0):
        k=(int(a[i])*(2**(-i-1)))
        s=s+k
        i=i+1
    if (s%7==0):
        response+="<b> It is divisible by 7 </b><br>" 
    else:
         response+="<b> It is not divisible by 7 </b><br>"
    
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
