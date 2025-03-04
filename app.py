from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded credentials (for testing)
VALID_USERNAME = "admin"
VALID_PASSWORD = "securepassword"

# HTML template for login page
login_form = """
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
    <h2>Login Page</h2>
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    <p>{{ message }}</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            message = "Login Successful!"
        else:
            message = "Invalid username or password"

    return render_template_string(login_form, message=message)

if __name__ == "__main__":
    app.run(debug=True)
