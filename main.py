from flask import Flask, render_template, request
import pandas as pd 
import numpy as np 
from txt_smry import summary_func

import os
os.environ["PYTHONIOENCODING"] = "utf-8"

app = Flask(__name__)

@app.route('/')
def index():
	data = pd.read_csv('csv_file_cobalt_chloride_humid_air_colour_papers - csv_file_cobalt_chloride_humid_air_colour_papers.csv')
	data = data.astype(str)
	abstracts = data.iloc[:, 2].values
	titles = data.iloc[:, 8].values
	return render_template('index.html', titles = titles)

@app.route('/page', methods=['GET', 'POST'])
def page():
	if request.method == "POST":
		title = request.form.get("titles", None)

		data = pd.read_csv('csv_file_cobalt_chloride_humid_air_colour_papers - csv_file_cobalt_chloride_humid_air_colour_papers.csv')
		data = data.astype(str)
		abstracts = data.iloc[:, 2].values
		t = data.iloc[:, 8].values

		c = 0
		for i in range(len(t)):
			if t[i] == title:
				my_abstract = abstracts[i]
	#			my_abstract = abstracts[i]
			c+=1

		summary = summary_func(my_abstract)
		if summary == '':
			summary = 'Abstract is already too short OR nan'
	return render_template("page.html", title = title, my_abstract = my_abstract, titles = t, summary = summary)


if __name__ == '__main__':
    app.run(debug = True)
