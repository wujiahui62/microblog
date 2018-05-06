# Welcome to Microblog!

## Enhanced features added:
### 1. Added upload image, user can select to show the uploaded image or the avatar image

### 2. Show weather if the zipcode is given in the current user's user profile

### 3. Added a send me a copy link below each post to send a copy to current use's email address

#### Deployment on pythonanywhere

* go to the bash console of PA
```
cd mysite
git clone https://github.com/wujiahui62/microblog.git
cd microblog
mkvirtualenv --python=/usr/bin/python3.6 my-virtualenv
pip install flask
pip install -r requirements.txt
```
* disable the following line in start.sh
```
flask run
```
* change mode of the start.sh file and run start.sh
```
chmod +x /home/Jiahui/mysite/microblog/start.sh
./start.sh
```
* Reload, done


#### References

[combine flask-wtf and flask-uploads](http://www.patricksoftwareblog.com/tag/flask-uploads/)

[deploy on pythonanywhere](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-three)
