from flask import Flask, render_template
from controllers.managers_controller import managers_blueprint
from controllers.deletions_controller import deletions_blueprint

app = Flask(__name__) 

app.register_blueprint(managers_blueprint)
app.register_blueprint(deletions_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title="Home") 

if __name__ == "__main__": 
    app.run(debug=True)