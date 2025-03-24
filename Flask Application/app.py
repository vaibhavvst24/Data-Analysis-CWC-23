from flask import Flask, render_template
import pandas as pd

# Create Flask app
app = Flask(__name__)

# Load dataset
DATA_FILE = ("CWC2023.csv")
cwc_data = pd.read_csv(DATA_FILE)

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# Visualizations route
@app.route('/visualisation')
def visualisations():
    return render_template('visualisation.html')

if __name__ == '__main__':
    app.run(debug=True)
