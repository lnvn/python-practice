from flask import Flask, request, Response
import hashlib
import os

app = Flask(__name__)

# A mock username and password for demonstration purposes
USERNAME = "admin"
PASSWORD = "secret"

# A mock realm for authentication
REALM = "Secure Area"

def generate_ha1(username, realm, password):
    """Generate the HA1 hash."""
    return hashlib.md5(f"{username}:{realm}:{password}".encode()).hexdigest()

def generate_ha2(method, uri):
    """Generate the HA2 hash."""
    return hashlib.md5(f"{method}:{uri}".encode()).hexdigest()

def generate_response(ha1, ha2, nonce, nc, cnonce, qop):
    """Generate the response hash."""
    return hashlib.md5(f"{ha1}:{nonce}:{nc}:{cnonce}:{qop}:{ha2}".encode()).hexdigest()

@app.route('/secure')
def secure_page():
    auth = request.headers.get("Authorization")

    # If no Authorization header, prompt for credentials
    if not auth or not auth.startswith("Digest "):
        return digest_auth_challenge()

    # Parse the Authorization header
    auth_values = parse_auth_header(auth[7:])
    
    # Validate credentials
    if not validate_credentials(auth_values):
        return digest_auth_challenge()

    return "You have successfully authenticated with Digest Authentication!"

def digest_auth_challenge():
    """Send a 401 Digest Authentication challenge."""
    nonce = os.urandom(16).hex()  # Generate a random nonce
    response = Response(status=401)
    response.headers["WWW-Authenticate"] = (
        f'Digest realm="{REALM}", '
        f'qop="auth", '
        f'nonce="{nonce}", '
        f'opaque="{hashlib.md5(REALM.encode()).hexdigest()}"'
    )
    return response

def parse_auth_header(header):
    """Parse the Digest Authorization header into a dictionary."""
    auth_values = {}
    for item in header.split(", "):
        key, value = item.split("=")
        auth_values[key.strip()] = value.strip('"')
    return auth_values

def validate_credentials(auth_values):
    """Validate the digest authentication credentials."""
    ha1 = generate_ha1(USERNAME, REALM, PASSWORD)
    ha2 = generate_ha2(request.method, auth_values["uri"])
    response = generate_response(
        ha1,
        ha2,
        auth_values["nonce"],
        auth_values["nc"],
        auth_values["cnonce"],
        auth_values["qop"],
    )
    return response == auth_values["response"]

if __name__ == '__main__':
    app.run(debug=True)
