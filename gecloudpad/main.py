from flask import Flask,redirect
app = Flask(__name__)
import requests
from xml.etree import ElementTree

app.config.from_pyfile('default_config.py')
# bonus config
app.config.from_envvar('GECLOUDPAD_SETTINGS',silent=True)

@app.route('/')
def hello():
    response = requests.get('http://blog.binaergewitter.de/latest-show')
    prev = int(response.content)
    return redirect(f"{app.config['BASEURL']}/p/bgt{prev+1}")

if __name__ == '__main__':
    app.run()
