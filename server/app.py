import json
from flask import Flask, jsonify, request
app = Flask(__name__)
import pandas;

@app.route('/getData', methods=['POST'])
def get_employees():
 data = json.loads(request.data)['query']
 updatedData = data.strip()
 df = pandas.read_csv('Discovery.csv')
 filtered = eval(updatedData)
 if isinstance(filtered, int):
   updated={
    "type": "int",
    "res": json.dumps(filtered)
   }
   return updated
 if filtered.empty:
   updatedRes={
    "type": "string",
    "res": json.dumps('No relevant data found in the report')
   }
   return updatedRes
 response = filtered.to_json(orient='records')
 res={
    "type": "obj",
    "res": response
   }
 return res

if __name__ == '__main__':
   app.run(port=3003)
