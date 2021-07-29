#! /bin/bash
yum update -y
yum install python3 -y
pip3 install flask
cd /home/ec2-user
wget https://raw.githubusercontent.com/serdarcw/my-repository/master/Project-001-Roman-Numerals-Converter/app.py
mkdir templates
cd templates
wget https://raw.githubusercontent.com/serdarcw/my-repository/master/Project-001-Roman-Numerals-Convertetemplates/index.html
wget https://raw.githubusercontent.com/serdarcw/my-repository/master/Project-001-Roman-Numerals-Convertetemplates/result.html
cd ..
python3 app.py