from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	esa = "Ola q ase"
	return render_template('index.html', efa=esa)

if __name__ == '__main__':
   app.run()