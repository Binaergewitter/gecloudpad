from flask import Flask,redirect
app = Flask(__name__)
import requests
from xml.etree import ElementTree

base_url = os.environ.get('BASEURL','https://board.net')
@app.route('/')
def hello():
    response = requests.get('http://blog.binaergewitter.de//podcast_feed/talk/opus/rss.xml?feed_size=1')
    tree = ElementTree.fromstring(response.content)
    prev = int(tree[0][-1][0].text.split('#')[1].split(':')[0])
    return redirect(f"{base_url}/p/{prev+1}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
