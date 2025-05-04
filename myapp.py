from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<int:numbar>")
def hello_world(numbar):
    posts = [
        {
            "title": "記事のタイトル",
            "body": "記事の内容",
            "created_at": "2025-05-02",
        },
        {
            "title": "記事のタイトル2",
            "body": "記事の内容2",
            "created_at": "2025-05-02",
        },
        {
            "title": "記事のタイトル3",
            "body": "記事の内容",
            "created_at": "2025-05-02",
        },
    ]
    post = posts[numbar]
    return render_template("base.html", post=post)
