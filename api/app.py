from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
app = Flask(__name__)
CORS(app, origins=["http://localhost:9000"])  # Allow only this origin
@app.route('/api/get_data/', methods=['GET'])
def hello_world():
    
    return jsonify(ok=True,message="naresh hello nehaaaa ")

if __name__ == '__main__':
    app.run(debug=True)
