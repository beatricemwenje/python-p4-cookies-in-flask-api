from flask import Flask, session, jsonify, make_response, request

app = Flask(__name__)

# Secret key is required for session encryption
app.secret_key = 'supersecretkey123'

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):
    # Set default session values if they don't exist
    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    # Prepare response
    response = make_response(jsonify({
        'session': {
            'session_key': key,
            'session_value': session[key],
            'session_accessed': session.accessed,
        },
        'cookies': [{cookie: request.cookies[cookie]}
            for cookie in request.cookies],
    }), 200)

    # Set a new cookie
    response.set_cookie('mouse', 'Cookie')

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
