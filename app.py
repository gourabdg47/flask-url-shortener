from flask import Flask, redirect, request, jsonify
from url_shortner import main, get_original_url, add_click, get_stat
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import sqlite3

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'randomTestTingKey'
jwt = JWTManager(app)

def conn_database(db_file):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route("/getToken", methods=['POST'])
def get_token():
    data = request.get_json()
    password = data.get('password')
    uname = data.get('username')

    status = verify_user(uname, password)
    if status:
        access_token = create_access_token(identity=uname)
        return jsonify(access_token=access_token), 200

    return jsonify(
        {
            'error': 'Username and Password are required'
        }
    )


@app.route("/signUp", methods=['POST'])
def signup():
    data = request.get_json()

    password = data.get('password')
    uname = data.get('username')
    email = data.get('email')

    if not uname or not password:
        return jsonify(
            {
                'error': 'Username and Password are required'
            }
        )

    hashed_password = generate_password_hash(password)

    try:
        conn = conn_database('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                       (uname, email, hashed_password))
        conn.commit()
        conn.close()
        return jsonify({'message': 'User created successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists'}), 409

def verify_user(username, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Prepare the SQL query to retrieve the user's hashed password
    query = 'SELECT password FROM users WHERE username = ?'
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    conn.close()

    if result:
        stored_password_hash = result[0]
        # Compare the stored hashed password with the provided password
        if check_password_hash(stored_password_hash, password):
            return True  # Authentication successful
        else:
            return False  # Incorrect password
    else:
        return False  # Username not found


@app.route("/<short_code>", methods=['GET'])
def url_redirect(short_code):
    url_data = get_original_url(short_code)
    print(f"ADD CLICK {url_data}, \n {type(url_data)}")

    if url_data :
        add_click(short_code, json_file="default.json")
        return redirect(url_data['url'], code=301)

    return "No data found...", 404  # Return a 404 if the URL is not found

@app.route("/stat/<short_code>", methods=['GET'])
def stat(short_code):
    url_data = get_stat(short_code)
    return str(url_data.get('clicks'))

@app.route("/", methods=['POST'])
def home():
    base_domain = request.host + '/'
    # BASE_DOMAIN = request.host_url

    data = request.get_json()
    if data:
        original_url = data.get('url')
    else:
        original_url = 'https://www.geeksforgeeks.org/system-design-url-shortening-service/#how-would-you-design-a-url-shortener-service-like-tinyurl'
    short_code = main(original_url)

    return base_domain + short_code


if __name__ == '__main__':
    app.run(debug=True)

