from flask import Flask

app = Flask(__name__)  ### object oluşturuyoruz
@app.route('/')   ## url'ye assıgn etmek lazım flaskte decorater denıyor
def hello():       ## kesme işareti main demek localhost 
    return 'Hello World!'

@app.route('/second')
def second():
    return 'Bize her yer Malatya'

@app.route('/third/subthird')
def third():
    return "This is the subpage of third page"

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}' ## burayı localhost:5000/forth/ numarayı kafadan sallıyoruz

if __name__ == '__main__':
    #app.run(debug = True) ## True modda çalısıyor. hata oldugunda hatayı geriye giderek çözüyor
    app.run(host='0.0.0.0', port=80)  # ec2 da calıstırmak ıcın yukarsı koment oldu