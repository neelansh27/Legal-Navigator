import os
from flask import Flask, json, render_template, send_from_directory,request, redirect, flash,url_for,session
from flask_sqlalchemy import SQLAlchemy
import chatbot3 as cb
# import pySQLcase as case
import summary as summ
import csv
from flask_session import Session
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("URI")
db = SQLAlchemy(app)

# Models
class case(db.Model):
    __tablename__='case'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(30))
    judge=db.Column(db.String(40))
    accused=db.Column(db.String(40))
    defendant_lawyer=db.Column(db.String(40))
    petitioner=db.Column(db.String(40))
    prosecution_lawyer=db.Column(db.String(40))
    description=db.Column(db.String(1200))
    court_name=db.Column(db.String(40))
    status=db.Column(db.String(40))
    filing=db.Column(db.Date)
    next_trail=db.Column(db.Date)

class hearing(db.Model):
    __tablename__="hearing"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    hdate=db.Column(db.Date)
    summary=db.Column(db.String(800))
    case_id=db.Column(db.Integer,db.ForeignKey('case.id'),nullable=False)

    

    
print("connected")
# Define the folder where your PDF files are stored
pdf_folder = "\\PDFs\\"  # Create a folder named "pdfs" and place your PDF files inside

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route('/')
def index():
    return render_template('entry_point.html')

@app.route('/home')
def home():
    return render_template('homepage.html')
@app.route('/chatbot',methods=['GET', 'POST'])
def chatbot():
    if request.method== "POST":
        user_input = request.form.get("user-msg")
        chat= request.form.get("chat")
        if chat:
            chat=json.loads(chat)
        else:
            chat=[]
        response = cb.chatbot_response(user_input)
        chat.append([user_input,response])
        return render_template("chatbot.html",chat=chat)
    return render_template("chatbot.html")


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with open("sample.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == username and row[1] == password:
                    session['username'] = username
                    flash('Login successful!', 'success')
                    return redirect(url_for('home'))

        flash('Invalid username or password. Please try again.', 'error')
        return redirect(url_for('login'))
    return render_template("login.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get("username")
        print(username)
        password = request.form.get('password')

        with open("sample.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row==[]:
                    break

                elif row[0] == username:
                    flash('Username already exists. Please choose a different username.', 'error')
                    return redirect(url_for('signup'))

        with open("sample.csv", mode='a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([username, password])

        flash('Account created successfully. You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route("/summary",methods=['GET', 'POST'])
def summary():
    if request.method=='POST':
        article=request.form.get('q')
        title,result=summ.get_article_summary("Article "+article)
        return render_template("summary1.html",title=title.split(':')[1],article=result)
    return render_template("summary1.html")

@app.route("/caseList")
def caseInfo():
    cases=case.query.all()
    return render_template('cases_list.html',cases=cases)

@app.route("/caseDetails/<id>")
def caseDetails(id):
    cases=case.query.filter_by(id=id).all()
    hear=hearing.query.filter_by(case_id=id).all()
    return render_template('case_details.html',case=cases[0],hearing=hear)

@app.route('/LegalDocuments')
def LegalDocuments():
    return render_template('legaldocs.html')

@app.route('/LegalDocuments/pdf/<filename>')
def serve_pdf(filename):
    try:
        # Serve the selected PDF file from the specified folder
        return send_from_directory(pdf_folder, filename)
    except FileNotFoundError:
        return "PDF not found", 404

@app.route('/ExpertTalk')
def experts():
    return render_template("expert_talk.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/logout')
def logout():
    return redirect("login")
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
