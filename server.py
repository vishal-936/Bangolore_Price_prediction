from flask import Flask,request,jsonify
app=Flask(__name__)
import util

@app.route('/hello')
def hello():
    return 'Hi ho'

@app.route('/get_locations')
def get_location_names():
    response=jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods=["GET","POST"])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])

    response=jsonify({
        'estimated_price':util.predict_price(bhk,total_sqft,bath,location)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__=="__main__":
    print('Starting server for banglore home price predictions')
    app.run()