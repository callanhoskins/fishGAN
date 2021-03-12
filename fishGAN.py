import os
import random
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/', methods=['GET'])
def base():
    images = os.listdir('/home/ubuntu/fishGAN/static/good-images')
    img = 'static/good-images/' + images[random.randint(0, len(images))]
    return render_template('index.html', img=img)

if __name__ == '__main__': 
    app.run(host='0.0.0.0')
