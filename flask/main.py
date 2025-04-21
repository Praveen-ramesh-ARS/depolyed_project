from flask import Flask,render_template,url_for,request,redirect,make_response,jsonify
from flask_mysqldb import MySQL


app = Flask(__name__) #app is a object

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Praveen@1993"
app.config["MYSQL_DB"] = "flask_db"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

@app.route("/database")
def flask_db():
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT * FROM USER_TBL")
	data = cursor.fetchall()
	return render_template("index.html",ALLdata=data)
	# return jsonify(data)



# @app.route("/")
# def homepage():
# 	return "hello Praveen"

# @app.route("/second")
# def secondFunction():
# 	return "hello secondpage"

# @app.route("/login/<name>/<int:age>")
# def login(name,age):
# 	return f"Hai {name} My age is {age}"
@app.route("/")
def HomePage():
	return render_template("home.html")

@app.route("/about")
def AboutPage():
	return render_template("about.html")

@app.route("/contact")
def ContactPage():
	return render_template("contact.html")

@app.route("/services")
def ServicesPage():
	return render_template("services.html")

@app.route("/login",methods=["POST","GET"])
def login():
	if request.method == "POST":
		username = request.form['user_name']
		password = request.form['password']
		res = make_response("hi iam cookie")
		res.set_cookie(username,password)
		# res.save()
		return res
		

		# return redirect(url_for("user",user=user))
		
	return render_template("login.html")
	
@app.route("/<user>")	
def user(user):

	return "<h1>welcome</h1>"
 
# @app.route('/<name>/')
# def table(name):
	
# 	return render_template('index.html',a=name)
# @app.route('/table/forloop/')
# def forloop():
# 	marks = [100,90,98,99,97]
# 	return render_template('index.html',m=marks)

# @app.route("/table/<clr>/")
# def color(clr):
# 	return render_template('index.html',clr=clr)

if __name__ == "__main__":
	# print(__name__)
	app.run(debug=True) # if click refresh value changed with use (debug=True,port=3333)
	