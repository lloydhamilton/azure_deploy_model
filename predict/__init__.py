import logging
import json
import azure.functions as func
import numpy as np
import joblib

model = joblib.load('predict/rf_clf.joblib')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('❗❗❗ Executing function...❗❗❗ ')
    test_data = req.get_json()
    test_data = np.array(test_data)
    logging.info('❗❗❗ Executing predictions...❗❗❗ ')
    predictions = model.predict(test_data)
    response = json.dumps(predictions.tolist())
    logging.info('❗❗❗ Returning predictions...❗❗❗ ')
    return func.HttpResponse(
        body=response,
        status_code=200,
        mimetype="application/json"
    )
