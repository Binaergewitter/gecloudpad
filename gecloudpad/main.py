from flask import Flask,redirect
app = Flask(__name__)
import requests
from xml.etree import ElementTree

app.config.from_pyfile('default_config.py')
# bonus config
app.config.from_envvar('GECLOUDPAD_SETTINGS',silent=True)

@app.route('/')
def hello():
    response = requests.get('http://blog.binaergewitter.de//podcast_feed/talk/opus/rss.xml?feed_size=1')
    tree = ElementTree.fromstring(response.content)
    prev = int(tree[0][-1][0].text.split('#')[1].split(':')[0])
    return redirect(f"{app.config['BASEURL']}/p/{prev+1}")

if __name__ == '__main__':
    app.run()
