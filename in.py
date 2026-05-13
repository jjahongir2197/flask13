from flask import Flask, render_template, request, redirect

app = Flask(__name__)

posts = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        title = request.form["title"]
        content = request.form["content"]

        posts.append({
            "title": title,
            "content": content
        })

        return redirect("/")

    return render_template("index.html", posts=posts)

@app.route("/post/<int:id>")
def post(id):

    selected_post = posts[id]

    return render_template(
        "post.html",
        post=selected_post
    )

if __name__ == "__main__":
    app.run(debug=True)
