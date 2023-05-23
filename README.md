# Proxy lifetime  

* Click Login button  
* Insert Username and Password  
* Manual solve captcha and click Enter  
* Parse and print result  

### How to start  
```bash
# create .env and insert Login and Password
cp .env.example .env

python -m venv venv
. venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

python lifetime.py
```