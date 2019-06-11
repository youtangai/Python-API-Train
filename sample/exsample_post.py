# coding:utf-8
import json
from flask import Flask, jsonify, make_response, request, Response

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post_json():
  json = request.get_json()  # Get POST JSON
  NAME = json['name']
  result = {
    "data": {
      "id": 1,
      "name": NAME
      }
    }
  return jsonify(result) 

if __name__ == "__main__":
  app.run()