from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def head():
    first="This is my first condition experience"
    return render_template("index.html",  message = False )


@app.route('/serdar')
def header():
    name = ["Serdar", "Fatih", "Ali", "Fatma", "Mostafa"]
    return render_template("body.html", object = name)


if __name__=="__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)