## request kutucuklara yazılan formları çekmeye yarıyor
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

## sqllite için gerekli environmentler https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./email.db' ##sqllite ile çalısırken extra bir yere baglanmaya gerek yok. mysql de servere baglanılıyor
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  ###developrler ıcın bır satır Trueya cevırlırse ıkaz alınıyor
db = SQLAlchemy(app)         

# users tablosu olusturuyoruz...sql komutlarıyla tablo olusturuyoruz
drop_table = 'DROP TABLE IF EXISTS users;' ### users ısımlı tablo olusturmak ıstıyoruz.bu satır daha once varsa boyle bı tablo siler
users_table = """                           
CREATE TABLE users(
username VARCHAR NOT NULL PRIMARY KEY,
email VARCHAR);
"""
data= """
INSERT INTO users
VALUES
    ("Firuz Hakan", "firuzhakan@amazon.com"),
    ("Fatma", "fatma@google.com"),
    ("Nezih", "nezih@tesla.com");
"""
## yukardakı sql sadece 1 defa ıcra edilir..yanı 2.defa çalıstıracagın zaman silinir.sürekli calıstıracaksak kodları sılmek lazım fıruzhakan satırlarını ustunu
db.session.execute(drop_table)   ## bu komutlarla bunu icra et
db.session.execute(users_table)
db.session.execute(data)
db.session.commit()              ## en sonda commit ediyor

def find_email(keyword):       ## % ler başı ve sonundakıne bakmadan kelımeyı buluyor
    query = f"""
    SELECT * FROM users WHERE username like '%{keyword}%';
    """
    result = db.session.execute(query)
    user_emails = [(row[0], row[1]) for row in result] # yukardakı firuzhakan row0 mailim row1
    if not any(user_emails):
        user_emails = [("Not Found", "Not Found")]
    return user_emails


# yeni emailleri users tablosuna girecek ınssert email tanımlayacagız
def insert_email(name,email):
    query = f"""
    SELECT * FROM users WHERE username like '{name}' 
    """
    result = db.session.execute(query)
    response = ''
    if name == None or email == None:  ## boş bırakamazsın 
        response = 'Username or email can not be empty!!'
    elif not any(result):   ##yukardakılerden farklı ise (nezih,fatma insert et database)
        insert = f"""
        INSERT INTO users
        VALUES ('{name}', '{email}');
        """
        result = db.session.execute(insert)
        db.session.commit()
        response = f"User {name} and {email} have been added successfully"
    else:
        response = f"User {name} already exist"  ##mükererr girişi önlüyor. firuzhakan zaten var
    return response

@app.route('/', methods = ['POST', 'GET'])  ## anasayfamızı decorete edıyouz
def emails():
    if request.method == 'POST':  ## requstle gıılıen degerı cekıp deeğişkene atıyoruz
        user_app_name = request.form['user_keyword']
        user_emails = find_email(user_app_name)
        return render_template('emails.html', show_result = True, keyword = user_app_name, name_emails = user_emails)
    else:
        return render_template('emails.html', show_result = False) 

@app.route('/add', methods=['GET', 'POST'])
def add_email():
    if request.method == 'POST':
        user_app_name = request.form['username']
        user_app_email = request.form['useremail']
        result_app = insert_email(user_app_name, user_app_email)
        return render_template('add-email.html', result_html=result_app, show_result=True)
    else:
        return render_template('add-email.html', show_result=False)   
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=80)     