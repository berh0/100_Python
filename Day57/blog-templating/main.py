from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
print(response)
post_objects = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in response]

@app.route('/')
def home():
    return render_template("index.html", posts = post_objects)

@app.route('/blog/<int:postid>')
def get_post(postid):
    requested_post = None
    for post in post_objects:
        if post.post_id == postid:
            requested_post = post
    return render_template("post.html", post = requested_post)

if __name__ == "__main__":
    app.run(debug=True)