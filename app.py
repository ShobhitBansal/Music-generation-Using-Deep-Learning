from flask import Flask, render_template, redirect, request
import GenerateMusic as gm

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/', methods= ['POST'])
def disease():
	if request.method == 'POST':

		gm.generateMID()
		output = "Generated Music"
		return render_template("index.html", result = output)


if __name__ == '__main__':
	app.run(threaded = False)