from flask import Flask, request
from flask import render_template
#from flaskwebgui import FlaskUI
from mba_data_access import returnImg
import requests
from matplotlib import pyplot as plt
import numpy as np
import json
from PIL import Image
from io import BytesIO
import cv2
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import os

app = Flask(__name__)
#ui = FlaskUI(app) #browser_path=r"E\chrome\chrome.exe"

@app.route("/", methods = ['POST', 'GET'])
def hello():
	kernSize = 0
	thresSize = 0
	file = os.path.join('static', 'test.png')
	return render_template('index.html', kernSize = kernSize, thresSize = thresSize, file = file)


@app.route("/home", methods = ['POST', 'GET'])
def home():
	if request.method == 'POST':
		#img = spaceReturn()
		kernSize = int(request.form['kernSize'])
		thresSize = int(request.form['thresSize'])
		img = returnImg(kernSize, thresSize)
		file = os.path.join('static', 'test.png')
		print(file)
	return render_template('index.html', kernSize = kernSize, thresSize = thresSize, file = file)

if __name__ == "__main__":
    app.run(debug=True)
