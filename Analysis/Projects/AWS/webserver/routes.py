from webserver import webserver
import dill as pickle
import json
import pandas as pd
import numpy as np
from flask import request
from collections import OrderedDict
#export PYTHONPATH=$PYTHONPATH'/home/ubuntu/default:'
import custom_pipeline

PATH = '/home/ubuntu/default/webserver/'

DATA_TEST = pickle.load(open(PATH+'generate.pkl', 'rb'))
fraud_model = pickle.load(open(PATH+'pred.pkl', 'rb'))

@webserver.route('/')
@webserver.route('/generate')
def generate():

    out = "<br>".join([k+"="+str(list(v.values())[0])+"&" for k,v in DATA_TEST.sample(1).to_dict().items()])[:-1]
    api_call = "https://18.232.163.78:5000/default?<br>"+out
    
    return api_call

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
@webserver.route('/default')
def default():

    isoF_X = pickle.load(open(PATH+'isoF_X.pkl', 'rb'))
    isoF = pickle.load(open(PATH+'isoF.pkl', 'rb'))
    isoF.offset_ = -.5
    isoF_pop = pickle.load(open(PATH+'isoF_pop.pkl', 'rb'))
    DATA2PREDICT = pd.DataFrame(columns=DATA_TEST.columns, index=[0])
    isoF_X = pd.DataFrame(columns=isoF_X.columns, index=[0])
    
    for k in request.args:
        tmp = request.args.get(k)
        if tmp == 'nan':
            tmp = np.nan
        if tmp == 'True' or tmp == 'False':
            tmp = bool(tmp)
        if is_number(tmp):
            tmp = float(tmp)
        DATA2PREDICT[k] = tmp

    DATA2ISOF = fraud_model.transform(DATA2PREDICT)
    for k in isoF_X:
        if k in DATA2ISOF:
            isoF_X[k] = DATA2ISOF[k]
    isoF_X.fillna(0, inplace=True)

    FPC = (1/100)*0.01*DATA_TEST.sum_paid_inv_0_12m.mean()
    if not DATA2PREDICT.sum_paid_inv_0_12m.isna().values[0]:
        FPC = (1/100)*0.01*DATA2PREDICT.sum_paid_inv_0_12m.values[0]
    FNC = DATA_TEST.num_unpaid_bills.mean()*DATA_TEST.avg_payment_span_0_12m.mean()
    if not DATA2PREDICT.num_unpaid_bills.isna().values[0] and not DATA2PREDICT.avg_payment_span_0_12m.isna().values[0]:
        FNC = DATA2PREDICT.num_unpaid_bills.values[0]*DATA2PREDICT.avg_payment_span_0_12m.values[0]

    pop_ave = 0.014453333333333334
    pr_pred = fraud_model.predict_proba(DATA2PREDICT)[0,1]

    result = [('Default_Prediction', int(fraud_model.predict(DATA2PREDICT)[0])),
              ('Default_Probability', np.round(pr_pred,4)),
              ('Relative_Risk_Ratio', np.round(pr_pred/pop_ave,3)),
              ('Extrapolation_Percentile', np.round(100*(isoF.decision_function(isoF_X)[0]<isoF_pop).mean(),1)),
              ('Cost_of_Actualized_False_Positive', "$"+"{:.2f}".format(np.round(FPC,2))),
              ('Cost_of_Actualized_False_Negative', "$"+"{:.2f}".format(np.round(FNC,2))),
              ('Long_Run_False_Positive_Cost', "$"+"{:.2f}".format(np.round(FPC*(1-pr_pred),2))),
              ('Long_Run_False_Negative_Cost', "$"+"{:.2f}".format(np.round(FNC*pr_pred,2)))]
    result = OrderedDict(result)
              
    result = json.dumps(result).replace(',',',<br>').replace('{','{<br>').replace('}','<br>}')

    return result
    
