from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)
id = 0
@app.route('/')
def index():
    mysql = connectToMySQL('first_flask')	        # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html", all_friends=friends)
	
@app.route("/create_user", methods=["POST"])
def add_user_to_db():
    return render_template("users.html")
    
@app.route("/home", methods=["POST"])
def go_home():
    return redirect("index.html")
    
@app.route("/destroy", methods=["POST"])
def destroy():
    global id
    mysql = connectToMySQL("first_flask")	        # call the function, passing in the name of our db
    query = "DELETE FROM friends WHERE id=1;"
    data = {
    
        "id": id,
        
    }
    delete_user_id = mysql.query_db(query, data)
    return redirect("/")

@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    id_from_form = request.form['id']
    fname_from_form = request.form['fname']
    lname_from_form = request.form['lname']
    occ_from_form = request.form['occ']
    id = id_from_form
    mysql = connectToMySQL("first_flask")	        # call the function, passing in the name of our db
    query = "INSERT INTO friends (id, first_name, last_name, occupation, created_at, updated_at) VALUES (%(id)s, %(fn)s, %(ln)s, %(occup)s, NOW(), NOW());"
    data = {
    
        "id": request.form['id'],
        "fn": request.form['fname'],
        "ln": request.form['lname'],
        "occup": request.form['occ']
        
    }
    new_user_id = mysql.query_db(query, data)
    return render_template("show.html", id_on_template=id_from_form, fname_on_template=fname_from_form, lname_on_template=lname_from_form, occ_on_template=occ_from_form)
	
if __name__ == "__main__":
    app.run(debug=True)
