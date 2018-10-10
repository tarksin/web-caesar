from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config["DEBUG"] = True


form="""
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
        </style>
    </head>
    <body>
          <form action="" method="POST">
            <label>Rotate by:</label>
            <input type="text" name="rot" value="0">
        <br>    <textarea width="200"  height="75" name="text">{0}</textarea>
        <br>    <input type="submit" value="Submit Query">

          </form>


    </body>
</html>
 """


@app.route('/', methods=["GET","POST"])
def encrypt():
    text_area_text = ''
    if request.method == "POST":
        text=request.form['text']
        rot=request.form['rot']
        text_area_text = rotate_string(text, int(rot))
        return form.format(text_area_text)
            
    return form.format(text_area_text)

@app.route('/asdfasdfasdf')
def index():
    return form


app.run()
