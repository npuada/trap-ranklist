import ranklist
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	trap_ranklist = ranklist.get_ranklist()
	return render_template('index.html', ranklist=trap_ranklist)


if __name__ == '__main__':
	app.run()
