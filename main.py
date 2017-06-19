from flask import Flask, request
from caesar import rotate_string

# set up Flask app with debugging on for easier error detection

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}

            h1 {{
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>Web Caesar</h1>
        </header>
        <form action="/" method="POST">
            <label for="rotate_by">Rotate by:</label>
            <input id="rotate_by" type="text" name="rot" value="0" />
            <textarea id="txtArea" name="text">{0}</textarea>
            <input type="submit" value='Encrypt Message!'/>
        </form>
    </body>

</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
#Caesar cipher encryption function taking inputs 'text' and the degree of rotation
    text = request.form['text']
    rot = request.form['rot']
    jumbled_text = rotate_string(str(text), int(rot))
    return form.format(jumbled_text)

app.run()