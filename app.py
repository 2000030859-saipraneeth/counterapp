from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='template')

volume_path = '/app_volume' 

def get_current_value():
    try:
        with open(os.path.join(volume_path, 'value.txt'), 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0

def update_value(new_value):
    with open(os.path.join(volume_path, 'value.txt'), 'w') as file:
        file.write(str(new_value))

@app.route('/')
def index():
    current_value = get_current_value()
    return render_template('index.html', current_value=current_value)

@app.route('/increment', methods=['POST'])
def increment():
    current_value = get_current_value()
    new_value = current_value + 1
    update_value(new_value)
    return str(new_value)

@app.route('/decrement', methods=['POST'])
def decrement():
    current_value = get_current_value()
    new_value = current_value - 1
    update_value(new_value)
    return str(new_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)
