from flask import Flask, render_template, request

app = Flask(__name__)

def convert(decimal_num):
    #I'll write a function named 'convert' and I'll pass an argument decimal_number. I'll convert this number into roman numeral. For sake of this project, you should be familiar with the coding a little bit. Your python knowledge is enough to solve this problem I thing. I'll use dictionary which has numbers as keys and their roman numbers as values. (the Roman numeral equivalent of this number)
    roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    # I create an empty string and it will hold my roman number
    num_to_roman = ''
    # I'll use for loop to create result. I'll divide the decimal number by dictionary keys from top to the end. I need to find out how many for example 1000 does decimal_num has. And then I'll multiply this number with value of key. 
    for i in roman.keys():
        num_to_roman += roman[i]*(decimal_num//i) # (decimal_num//i) gives us quotient of division
        # I need to get remainder of division of decimal_num by i
        decimal_num %= i
    return num_to_roman
    # Try a couple of examples. Of course, you all might have different function

@app.route('/', methods=['POST', 'GET'])
def main_post():
    if request.method == 'POST' : # girilen metod post sa sayıyı hesaplayacak degilse index htmli cıkaracak
        alpha = request.form['number'] ##alpha değişkenine atadık
        if not alpha.isdecimal(): # burada kontrol yapacagız. sayı olmayan girdilerde uyarı verecek
             return render_template('index.html', developer_name ='Firuz Hakan', not_valid=True)
        number=int(alpha)                  # girilen sayının 0-4000 arasında olması koşulunu yapıyporuz
        if not 0 < 4000 :
            return render_template('index.html', developer_name ='Firuz Hakan', not_valid=True)  # hata mesajı 
        return render_template('result.html', number_decimal=number, number_roman=convert(number), developer_name='Firuz Hakan')
    else:
         return render_template('index.html', developer_name ='Firuz Hakan', not_valid=False)  # hata mesajı 




if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host= '0.0.0.0', port=80)

