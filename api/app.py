from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app, origins=["http://localhost:9000"])  # Allow only this origin

# Secret key for session management
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/get_data/', methods=['GET'])
def hello_world():
    return jsonify(ok=True, message="naresh hello nehaaaa")

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    print(f"Received signup data: {data}")  # Debugging output

    # Check if username already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 409

    # Hash the password before storing it using pbkdf2:sha256
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    print(hashed_password, "hashed password")  # Debugging output

    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    print(user, "user checkkkkkkkk")
    print(f"Login attempt with username: {data['username']}")
    print(f"Login attempt with password: {data['password']}")

    if user and check_password_hash(user.password, data['password']):
        print("ckeckkkkk")
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful'}), 200
    
    return jsonify({'error': 'Invalid username or password'}), 401

@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Remove the user ID from session
    return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/api/add-expense', methods=['POST'])
def add_expense():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    data = request.json
    new_expense = Expense(user_id=session['user_id'], category=data['category'], amount=data['amount'])
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'category': data['category'], 'amount': data['amount']}), 201

@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    expenses = Expense.query.filter_by(user_id=session['user_id']).all()
    return jsonify([{'category': e.category, 'amount': e.amount} for e in expenses]), 200

if __name__ == '__main__':
    app.run(debug=True)
