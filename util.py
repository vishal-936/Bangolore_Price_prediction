import pickle
import json
import numpy as np

__columns=None
__location=None
__model=None

def get_location_names():
    return __location

def predict_price(bhk,total_sqrt,bath,location):
    try:
        loc=__columns.index(location.lower())
    except:
        loc=__columns.index('Whitefield'.lower())
    
    p=np.zeros(len(__columns))
    p[0],p[1],p[2]=bhk,total_sqrt,bath
    p[loc]=1
    return round(__model.predict([p])[0],2)

def load_essentials():
    global __columns
    global __location
    global __model
    with open('columns.json','r') as f:
        __columns=json.load(f)['data_columns']
        __location=__columns[3:]
    with open('banglore_home_price_prediction.pickle','rb') as f:
        __model=pickle.load(f)

    print('model,columns and location loaded')
load_essentials()
if __name__=='__main__':
    print(predict_price(4,2825,4,'1st Phase JP Nagar'))
    print(get_location_names())