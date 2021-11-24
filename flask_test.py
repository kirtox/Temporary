# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 16:49:24 2021

@author: asxz8
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        data = request.form

        print("POST!!")
        print("data\n=> ", data)
        return jsonify(data)
    
@app.route('/get', methods=['GET'])
def get():
    if request.method == 'GET':
        chillerId = request.args.get('chillerId')
        
        print("GET!!")
        print("data\n=> chillerId:", chillerId)
        return jsonify(chillerId)
    
if __name__=='__main__':
    app.run()
    #app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)    