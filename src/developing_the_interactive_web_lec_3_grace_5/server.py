from flask import Flask, render_template, request

app = Flask(__name__)

names = []
# def twice(some_funk):
#     def temp(*args, **argv):
#         some_funk(*args, **argv)
#         some_funk(*args, **argv)

# def say_moo():
#     print("moo")

# say_moo()

@app.route("/") # letting the app register itself as the function to call on url /
def hello_world():
    return render_template("hello.html")
    # return "<p>Hello, World!</p>"

@app.route("/catch", methods=["POST"])
def catch():
    # how do we get that data?
    global names

    if request.form.get("name"):
        names.append(request.form.get("name"))
    return render_template("hello.html", names=names)


"""
flask --app server.py run
basically allows you to take a file and have flask make it a server

@ sign in python makes a decorator


Ok so. You want templates, and to use it always!!!

"""