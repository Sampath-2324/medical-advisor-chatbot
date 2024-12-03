import subprocess  # To run the Tkinter script
from flask import Flask

app = Flask(__name__)

# This will directly run the Tkinter GUI script (QuestionDiagonosisTkinter.py)
def run_tkinter_app():
    subprocess.Popen(['python', 'QuestionDiagonosisTkinter.py'])

@app.route('/')
def home():
    # Directly run the Tkinter GUI script when the root route is accessed
    run_tkinter_app()
    return "The Tkinter window should now open on your desktop."

if __name__ == '__main__':
    # Run the Flask app, which will then trigger the Tkinter GUI
    app.run(debug=True)
