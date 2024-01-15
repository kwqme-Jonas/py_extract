from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)

CORS(app, origins=["http://localhost:3000"])
@app.route('/execute-script', methods=['POST'])
def execute_script():
    try:
        data = request.json
        index = data.get('index')
        addon = data.get('addon')

        # Add your Python script execution logic here
        result = subprocess.check_output(['python', 'C:\\Projects\\Extract_Py\\extract\\elastic_search\\run_python.py', '-index', index, '-addon', addon])

        return jsonify({'success': True, 'result': result.decode('utf-8')})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
